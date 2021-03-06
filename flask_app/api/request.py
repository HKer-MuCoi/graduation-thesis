# coding: utf8
from flask_restful import Resource
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.request import RequestService
from app.constants import Role

# ns = Namespace(name="request", description="request")


# @ns.route("")
class APIRequest(Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("status", location=['values', 'json'], required=False, help="status", type=int, default=None),
        Argument("due_date", location=['values', 'json'], required=False, help="due_date", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = RequestService.create(**kwargs)
        return resource

    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("id", location=['values', 'json'], required=False, help="id", type=str, default=None),
        Argument("due_date", location=['values', 'json'], required=False, help="due_date", type=str, default=None),
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = RequestService.update(**kwargs)
        return resource


# @ns.route("/<string:request_id>")
class APIRequestById(Resource):
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def get(self, request_id):
        resource = RequestService.get_by_id(request_id)
        return resource

    @check_token(role=[Role.HR.value])
    def delete(self, request_id):
        resource = RequestService.delete_by_id(request_id)
        return resource


# @ns.route("/<string:request_id>/unassign")
class APIRequestUnassigned(Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, request_id, **kwargs):
        kwargs['request_id'] = request_id
        resource = RequestService.remove_job_seeker(**kwargs)
        return resource


# @ns.route("/job-seeker/<string:job_seeker_id>")
class APIRequestByJobSeeker(Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
    )
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def get(self, job_seeker_id, **kwargs):
        kwargs['job_seeker_id'] = job_seeker_id
        resource = RequestService.get_simple_request_response_by_job_seeker_id(**kwargs)
        return resource


# @ns.route("/referrer/<string:referrer_id>")
class APIRequestFindByReferrerId(Resource):
    # findByReferrerId
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def get(self, referrer_id):
        resource = RequestService.find_by_referrer_id(referrer_id)
        return resource


# @ns.route("/draft")
class APIRequestDraft(Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value])
    def get(self, **kwargs):
        resource = RequestService.find_by_type_and_job_seeker_is_null(**kwargs)
        return resource


# @ns.route("/assign-referrer")
class APIRequestAssignReferrer(Resource):
    # AssignReferrerDTO
    @parse_params(
        Argument("request_id", location=['values', 'json'], required=False, help="request_id", type=str, default=None),
        Argument("referrer_id", location=['values', 'json'], required=False, help="referrer_id", type=str,
                 default=None),
        Argument("relationship_type", location=['values', 'json'], required=False, help="relationship_type", type=str,
                 default=None),
        Argument("relationship_desc", location=['values', 'json'], required=False, help="relationship_desc", type=str,
                 default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = RequestService.assign_referrer(**kwargs)
        return resource


# @ns.route("/assign-job-seeker")
class APIRequestAssignJobSeeker(Resource):
    # AssignJobSeekerDTO
    @parse_params(
        Argument("request_id", location=['values', 'json'], required=False, help="request_id", type=str, default=None),
        Argument("job_seeker_id", location=['values', 'json'], required=False, help="job_seeker_id", type=str,
                 default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = RequestService.assign_job_seeker(**kwargs)
        return resource


# @ns.route("/data-select")
class APIRequestDataSelect(Resource):
    @parse_params(
        Argument("codeOrName", location=["args"], required=False, help="codeOrName", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value])
    def get(self, **kwargs):
        resource = RequestService.get_data_select(**kwargs)
        return resource


# @ns.route("/filter-table")
class APIRequestFilterTable(Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("to_due_date", location=['values', 'json'], required=False, help="to_due_date", type=str,
                 default=None),
        Argument("from_due_date", location=['values', 'json'], required=False, help="from_due_date", type=str,
                 default=None),
        Argument("job_seeker", location=['values', 'json'], required=False, help="job_seeker", type=str, default=None),
        Argument("referrer", location=['values', 'json'], required=False, help="referrer", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def post(self, **kwargs):
        resource = RequestService.filter_table(**kwargs)
        return resource


# @ns.route("/filter-details")
class APIRequestFilterDetails(Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("to_due_date", location=['values', 'json'], required=False, help="to_due_date", type=str,
                 default=None),
        Argument("from_due_date", location=['values', 'json'], required=False, help="from_due_date", type=str,
                 default=None),
        Argument("to_created_at", location=['values', 'json'], required=False, help="to_created_at", type=str,
                 default=None),
        Argument("from_created_at", location=['values', 'json'], required=False, help="from_created_at", type=str,
                 default=None),
        Argument("job_seeker", location=['values', 'json'], required=False, help="job_seeker", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("referrer", location=['values', 'json'], required=False, help="referrer", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def post(self, **kwargs):
        resource = RequestService.filter_details(**kwargs)
        return resource


# @ns.route("/<string:request_id>/complete")
class APIRequestComplete(Resource):
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def put(self, request_id):
        resource = RequestService.complete(request_id)
        return resource


# @ns.route("/export-excel")
class APIRequestExportExcel(Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("to_due_date", location=['values', 'json'], required=False, help="to_due_date", type=str,
                 default=None),
        Argument("from_due_date", location=['values', 'json'], required=False, help="from_due_date", type=str,
                 default=None),
        Argument("job_seeker", location=['values', 'json'], required=False, help="job_seeker", type=str, default=None),
        Argument("referrer", location=['values', 'json'], required=False, help="referrer", type=str, default=None),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def post(self, **kwargs):
        resource = RequestService.export_excel(**kwargs)
        return resource
