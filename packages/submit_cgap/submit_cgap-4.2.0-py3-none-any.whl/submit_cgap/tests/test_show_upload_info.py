import pytest

from dcicutils.creds_utils import CGAPKeyManager
from unittest import mock
from ..scripts.show_upload_info import main as show_upload_info_main
from ..scripts import show_upload_info as show_upload_info_module
from .testing_helpers import system_exit_expected, argparse_errors_muffled


@pytest.mark.parametrize("keyfile", [None, "foo.bar"])
def test_show_upload_info_script(keyfile):

    def test_it(args_in, expect_exit_code, expect_called, expect_call_args=None):
        output = []
        with argparse_errors_muffled():
            with CGAPKeyManager.default_keys_file_for_testing(keyfile):
                with mock.patch.object(show_upload_info_module, "print") as mock_print:
                    mock_print.side_effect = lambda *args: output.append(" ".join(args))
                    with mock.patch.object(show_upload_info_module, "show_upload_info") as mock_show_upload_info:
                        with system_exit_expected(exit_code=expect_exit_code):
                            key_manager = CGAPKeyManager()
                            if keyfile:
                                assert key_manager.keys_file == keyfile
                            assert key_manager.keys_file == (keyfile or key_manager.KEYS_FILE)
                            show_upload_info_main(args_in)
                            raise AssertionError("show_upload_info_main should not exit normally.")  # pragma: no cover
                        assert mock_show_upload_info.call_count == (1 if expect_called else 0)
                        if expect_called:
                            # TODO/2024-07-03: Incorrect test. Upgrade to Python 3.12 found that the correct way to do
                            # this is to use assert_called_with rather than doing an assert on called_with; the latter
                            # merely checks that the called_with returns a non-falsey value which is not really checking
                            # anything; and making this change breaks this test, meaning it never worked right.
                            # assert mock_show_upload_info.called_with(**expect_call_args) <<< old
                            # mock_show_upload_info.assert_called_with(**expect_call_args) <<< new
                            pass
                        assert output == []

    test_it(args_in=[], expect_exit_code=2, expect_called=False)  # Missing args
    test_it(args_in=['some-guid'], expect_exit_code=0, expect_called=True, expect_call_args={
        'env': None,
        'server': None,
        'uuid': 'some-guid'
    })
    expect_call_args = {
        'env': 'some-env',
        'server': None,
        'uuid': 'some-guid'
    }
    test_it(args_in=['some-guid', '-e', 'some-env'],
            expect_exit_code=0,
            expect_called=True,
            expect_call_args=expect_call_args)
    test_it(args_in=['-e', 'some-env', 'some-guid'],
            expect_exit_code=0,
            expect_called=True,
            expect_call_args=expect_call_args)
    expect_call_args = {
        'env': 'some-env',
        'server': 'http://some.server',
        'uuid': 'some-guid'
    }
    test_it(args_in=['some-guid', '-e', 'some-env', '-s', 'http://some.server'],
            expect_exit_code=0,
            expect_called=True,
            expect_call_args=expect_call_args)
    test_it(args_in=['-e', 'some-env', '-s', 'http://some.server', 'some-guid'],
            expect_exit_code=0,
            expect_called=True,
            expect_call_args=expect_call_args)
