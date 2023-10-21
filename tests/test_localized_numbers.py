from datasette.app import Datasette
import pytest
import sqlite_utils


@pytest.fixture(scope="session")
def datasette(tmp_path_factory):
    db_directory = tmp_path_factory.mktemp("dbs")
    db_path = db_directory / "test.db"
    db = sqlite_utils.Database(db_path)
    db["numbers"].insert_all(
        [
            {"id": 1, "number_int": 1234567, "number_float": 1234567.50, "number_str": "1234567"},
        ],
        pk="id",
    )
    datasette = Datasette(
        [db_path],
        metadata={
            "databases": {
                "test": {
                    "tables": {
                        "numbers": {"title": "Some numbers"}
                    }
                }
            }
        },
    )
    return datasette


@pytest.mark.asyncio
async def test_plugin_is_installed(datasette):
    response = await datasette.client.get("/-/plugins.json")
    assert response.status_code == 200
    installed_plugins = {p["name"] for p in response.json()}
    assert "datasette-localized-numbers" in installed_plugins


@pytest.mark.asyncio
async def test_sql_function_int(datasette):
    response = await datasette.client.get(
        "/test.json?_shape=array&sql=select+localized_number(number_int)+AS+test+from+numbers"
    )
    assert response.status_code == 200
    assert response.json() == [{"test": "1\u00a0234\u00a0567"}]


@pytest.mark.asyncio
async def test_sql_function_float(datasette):
    response = await datasette.client.get(
        "/test.json?_shape=array&sql=select+localized_number(number_float)+AS+test+from+numbers"
    )
    assert response.status_code == 200
    assert response.json() == [{"test": "1\u00a0234\u00a0567,5"}]


@pytest.mark.asyncio
async def test_sql_function_str(datasette):
    response = await datasette.client.get(
        "/test.json?_shape=array&sql=select+localized_number(number_str)+AS+test+from+numbers"
    )
    assert response.status_code == 200
    assert response.json() == [{"test": "1\u00a0234\u00a0567"}]

