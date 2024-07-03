import os


def init_trino(
    cluster_name: str = None,
    host: str = "gateway-idp-prd.sktai.io",
    port: int = 443,
    connect_args: dict = None,
    user: str = None,
    password: str = None,
    extra_connect_args: dict = None,
):
    from sqlalchemy import create_engine
    from trino.sqlalchemy import URL

    nb_user = os.environ.get("NB_USER", "skt")

    # jovyan: NES로 실행 시 Jupyter 이미지일 경우 NB_USER가 jovyan으로 설정된다.
    # skt: 임의의 장소에서 패키지를 실행했을 경우 NB_USER 값이 없을 수 있는데, 이럴 경우 skt로 설정한다.

    if cluster_name is None:
        cluster_name = "aidp-cluster" if nb_user in ["jovyan", "skt"] else "aidp-interactive"

    extra_connect_args = extra_connect_args or {}
    connect_args = connect_args or {
        "extra_credential": [("cluster_name", cluster_name)],
        "http_scheme": "https",
        **extra_connect_args,
    }

    engine = create_engine(
        URL(host=host, port=port, user=user or nb_user, password=password),
        connect_args=connect_args,
    )

    try:
        from IPython import get_ipython

        ipython = get_ipython()
        if ipython:
            ipython.run_line_magic("load_ext", "sql", 1)
            ipython.run_line_magic("alias_magic", "trino sql", 1)
            ipython.run_line_magic("sql", "engine", 1)
    except ImportError:
        print("IPython not found, skipping magic commands")

    return engine
