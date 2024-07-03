import os


def read_configuration_from_env() -> dict[str, str]:
    return {
        "database_id": os.getenv("MORPH_DATABASE_ID"),
        "base_url": os.getenv("MORPH_BASE_URL"),
        "team_slug": os.getenv("MORPH_TEAM_SLUG"),
        "api_key": os.getenv("MORPH_API_KEY"),
        "canvas": os.getenv("MORPH_CANVAS"),
    }
