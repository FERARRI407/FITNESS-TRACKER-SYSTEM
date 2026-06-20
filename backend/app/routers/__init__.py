# Import all routers
from . import auth_router
from . import users_router
from . import goals_router
from . import dashboard_router
from . import workouts_router
from . import progress_router
from . import meals_router

__all__ = [
    "auth_router",
    "users_router",
    "goals_router",
    "dashboard_router",
    "workouts_router",
    "progress_router",
    "meals_router"
]



