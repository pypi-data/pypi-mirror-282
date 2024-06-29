import os

from create_api_app.utils.helper import get_dirpaths


class SetupAssetsDirNames:
    """A storage container for setup asset directory names."""

    ROOT = "setup_assets"
    FRONTEND = "frontend"
    BACKEND = "backend"
    APP = "app"

    UPLOADTHING = "uploadthing"


class AssetFilenames:
    """A storage container for asset filenames."""

    POETRY_CONF = "pyproject.toml"
    README = "README.md"

    MAIN = "main.py"
    BUILD = "build.py"

    TAILWIND = "tailwind.config.ts"
    NEXT_CONFIG = "next.config.mjs"


class SetupDirPaths:
    """A storage container for setup asset filepaths."""

    DIRPATHS_DICT = get_dirpaths("create_api_app", "setup_assets")

    BACKEND_ASSETS = DIRPATHS_DICT[SetupAssetsDirNames.BACKEND]
    FRONTEND_ASSETS = DIRPATHS_DICT[SetupAssetsDirNames.FRONTEND]
    ROOT_ASSETS = DIRPATHS_DICT["root"]
    UPLOADTHING_ASSETS = DIRPATHS_DICT[SetupAssetsDirNames.UPLOADTHING]


def __dotenv_setter(name: str, value: str) -> None:
    os.environ[name] = value


def set_project_name(name: str) -> None:
    __dotenv_setter("PROJECT_NAME", name)


def set_exclude_value(value: str) -> None:
    __dotenv_setter("EXCLUDE", value)


def set_poetry_version(version: str) -> None:
    __dotenv_setter("POETRY_VERSION", version)


def get_project_name() -> str:
    return os.environ.get("PROJECT_NAME")


def get_exclude_value() -> str:
    return os.environ.get("EXCLUDE")


def get_poetry_version() -> str:
    return os.environ.get("POETRY_VERSION")


class ProjectPaths:
    """A storage container for project directory and filename paths."""

    def __init__(self, project_name: str = None) -> None:
        self.PROJECT_NAME = project_name if project_name else get_project_name()
        self.ROOT = os.path.join(os.path.dirname(os.getcwd()), self.PROJECT_NAME)
        self.BACKEND = os.path.join(self.ROOT, SetupAssetsDirNames.BACKEND)
        self.BACKEND_APP = os.path.join(self.BACKEND, SetupAssetsDirNames.APP)
        self.FRONTEND = os.path.join(self.ROOT, SetupAssetsDirNames.FRONTEND)

        self.POETRY_CONF = os.path.join(self.BACKEND, AssetFilenames.POETRY_CONF)

        self.TAILWIND_CONF = os.path.join(self.FRONTEND, AssetFilenames.TAILWIND)

        self.ENV_LOCAL = os.path.join(self.ROOT, ".env.local")
        self.SETTINGS = os.path.join(self.BACKEND_APP, "config", "settings.py")
        self.MODELS = os.path.join(self.BACKEND_APP, "models", "__init__.py")

        self.PACKAGE_JSON = os.path.join(self.FRONTEND, "package.json")
        self.NEXT_CONF = os.path.join(self.FRONTEND, "next.config.mjs")
        self.SHAD_CONF = os.path.join(self.FRONTEND, "components.json")
        self.LAYOUT = os.path.join(self.FRONTEND, "src", "app", "layout.tsx")
        self.HOMEPAGE = os.path.join(
            self.FRONTEND, "src", "pages", "Homepage", "Homepage.tsx"
        )
