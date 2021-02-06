import pytest
import workshop.main as main

from click.testing import CliRunner


@pytest.mark.cli
def test_cli():
    runner = CliRunner()

    result = runner.invoke(main.main)

    assert not result.exception
    assert result.output == 'The total cost of your items is $0.00\n'
