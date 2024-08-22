import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def makeShellContext ():
    return {"sa": sa, "so": so, "db": db, "User": User, "Post": Post};
