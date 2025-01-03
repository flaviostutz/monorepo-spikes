from venv import logger


def hello() -> str:
    """Test"""
    # lint should get those things
    if True:
        logger.info("Hello")
    return "Hello world!"


def allow(test: str) -> str:
    """Test"""
    # if True:
    #     return "TRUE"  # noqa: ERA001
    return f"HALO {test}"
