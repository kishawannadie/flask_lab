
from flask import Blueprint
from common import group
from common.Students import *
from common.StorageStrategies import *
from common.utils import *

bp = Blueprint('groupSQLite', __name__)

def GetGroup():
    if 'group' not in g:
        storage = DBStorage(request.blueprint)
        g.group = group.Group(storage, getWebIO()) 
    return g.group

@bp.route("/", methods=['GET'])
def index():
	return GetGroup().ShowGroup()

@bp.route("/add", methods=['POST'])
def add():
    return GetGroup().Add()

@bp.route("/showform/<int:id>")
def showform(id):
    return GetGroup().ShowForm(id)

@bp.route("/delete/<int:id>")
def deleteitem(id):
    return GetGroup().Delete(id)


@bp.app_template_test("HeadStudent")
def is_head(value):
    return isinstance(value, HeadStudent)

@bp.app_template_test("UnionOrganizer")
def is_union(value):
    return isinstance(value, UnionOrganizer)

@bp.app_template_test("studentExist")
def studentExist(id):
    return id > 0


@bp.teardown_request
def teardown_group(ctx):
    GetGroup().storage.Store()


@bp.route("/api/", methods=['GET'])
def apigroup():
    return GetGroup().APIGroup()


@bp.route("/api/", methods=['POST'])
def apiadd():
    return GetGroup().APIAdd()


@bp.route("/api/<int:id>", methods=['GET'])
def apiget(id):
    return GetGroup().APIGet(id)


@bp.route("/api/<int:id>", methods=['PUT'])
def apiset(id):
    return GetGroup().APISet(id)


@bp.route("/api/<int:id>", methods=['DELETE'])
def apidelete(id):
    return GetGroup().APIDelete(id)


