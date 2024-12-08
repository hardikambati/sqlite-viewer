from fastapi import (
    Request,
    APIRouter,
)
from fastapi.templating import Jinja2Templates

from service import DBService


router = APIRouter()


templates = Jinja2Templates(directory="app/templates")


# =============== DATA API's ===============


@router.get("/test")
async def test(request: Request, table_name: str):
    return {
        "data": "success"
    }


@router.get("/")
async def root(request: Request):
    """
    Base home page
    Shows list of all available tables in DB
    """
    db_service = DBService()
    table_name_list: list = db_service.get_all_tables()
    return templates.TemplateResponse(
        "list_tables.html",
        {
            "request": request,
            "table_name_list": table_name_list,
        }
    )


@router.get("/{table_name}")
async def get_table_records(request: Request, table_name: str):
    """
    Get records for a particular table
    """
    db_service = DBService()
    table_name_list: list = db_service.get_all_tables()
    columns: list = db_service.get_column_names(name=table_name)
    records: list = db_service.get_records_for_table(name=table_name)
    return templates.TemplateResponse(
        "records.html",
        {
            "request": request,
            "records": records,
            "columns": columns,
            "active_table_name": table_name,
            "table_name_list": table_name_list,
        }
    )
