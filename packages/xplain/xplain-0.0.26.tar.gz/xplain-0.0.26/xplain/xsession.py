from xplain import Ref_xplainsession
from xplain import XObject
import pandas as pd
import uuid
import os
import zipfile
import logging


class Xsession:
    """
       class for managing xplain session and calling Xplain Web API.
       Each Xsession instance could manage an individual xplain session.

       Example:
           >>> from xplain import Xsession
           >>> s1 = Xsession(url="myhost:8080", user="me",
           password="secret1")
           >>> s2 = XplainSession(url="my_other_host:8080", user="me",
           password="secret2")
           >>> s1.terminate()
           >>> s2.terminate()

       """

    def __init__(self, url='http://localhost:8080', user='user',
                 password='xplainData', httpSession=None,
                 jwt_dispatch_url=None,
                 jwt_cookie_name=None, jwt_token=None):
        if os.environ.get('xplain_url') is not None:
            url = os.environ.get('xplain_url')

        if os.environ.get('xplain_user') is not None:
            user = os.environ.get('xplain_user')

        if os.environ.get('xplain_password') is not None:
            password = os.environ.get('xplain_password')

        self._ref_session = Ref_xplainsession(url, user, password,
                                              httpSession,
                                              jwt_dispatch_url,
                                              jwt_cookie_name,
                                              jwt_token)

        if os.environ.get('xplain_session_id') is not None:
            session_id = os.environ.get('xplain_session_id')
            self._ref_session.load_from_session_id(session_id)

    def startup(self, startup_file):
        """
        load xplain session by given startup configuration file name without
        file extension

        :param startup_file: the file name of startup configuration,
        :type startup_file: string

        """
        self.set_default_broadcast(False)
        self._ref_session.startup(startup_file)

    def load_from_session_id(self, session_id):
        """
        load xplain session by given exisiting session id

        :param session_id: the 32 digit  xplain session id
        :type session_id: string
        """
        self.set_default_broadcast(True)
        self._ref_session.load_from_session_id(session_id)

    def terminate(self):
        """
        terminate the xplain session

        """
        self._ref_session.terminate()

    def get_session_id(self):
        """
        get the current xplain session id

        :return: session id
        :rtype: string
        """
        return self._ref_session.get_session_id()

    def show_tree(self):
        """
        show object hierarchy as tree

        """
        self._ref_session.show_tree()

    def run(self, method_call):
        """
        perform xplain web api method and broadcast the change to other
        client sharing with same session id

        :param method: xplain web api method in json format
        :type method: json

        """
        self._ref_session.run(method_call)

    def perform(self, method_call):
        """
         Send POST request against entry point /xplainsession with payload as
         json

        :param method_call: content of xplain web api
        :type method_call: json
        :return: request response
        :rtype: json

        Example
            >>> session.perform({"method": "deleteRequest",
                                  "requestName":"abcd"})
        """
        return self._ref_session.perform(method_call)

    def execute_query(self, query, data_frame=True):
        """
        execute the xplain request

        :param query: specification of the query
        :type query: Query_config or json
        :param data_frame: if True, the result will be returned as dataFrame
        :type data_frame: boolean
        :return:  result of given query
        :rtype:  JSON or DataFrame, depending on parameter dataFrame

        Example:
            >>> import xplain

            >>> session = xplain.Xsession()
            >>> session.startup('Patients')

            >>> # option 1, query config object
            >>>  query_config = xplain.Query_config()
            >>>  query_config.add_aggregation(
                                    object_name="Hospital Diagnose",
                                    dimension_name="Diagnose", type="COUNT")
            >>>  query_config.add_groupby(object_name="Hospital Diagnose",
                                          dimension_name="Diagnose",
                                          attribute_name="Type")
            >>> query_config.add_selection(object_name="Hospital Diagnose",
                                          dimension_name="Date_from",
                                          attribute_name="Date_from",
                                       selected_states=["2020-12"])
            >>> session.execute_query(query_config)

            >>> # option 2,  query in json
            >>> query = {
                    "aggregations" :[
                        {
                           "object": "AU-Diagnosen",
                           "dimension": "Diagnose",
                           "type": "SUM"
                       }
                    ],
                    "groupBys":[{
                       "attribute": {
                           "object": "Hospital Diagnose",
                           "dimension": "Diagnose",
                           "attribute": "Type"
                       }]
                }
            }
            >>> session.execute_query(query)
        """
        return self._ref_session.execute_query(query, data_frame)

    def open_query(self, query, data_frame=True):
        """
        perform the query and keep it open, the result of this query will be
        impacted by further modification of current session, like selection
        changes

        :param query: either xplain.Query instance or JSON
        :param data_frame: if True, the result will be returned as
        dataFrame
        :return:  result of given query
        :rtype:  JSON or DataFrame, depending on parameter dataFrame
        """
        return self._ref_session.open_query(query, data_frame)

    def print_error(self):
        self._ref_session.print_error()

    def get_queries(self):
        """
        get the list of the existing query ids

        :return: list of query ids
        :rtype: array of string
        """
        self._ref_session.get_queries()

    def resume_analysis(self, file_name):
        """
        resume the stored session

        :param file_name: name of stored session file
        :type file_name: string
        :return:  False (fail) or True (success)
        :rtype: Boolean
        """
        if ".xanalysis" not in file_name:
            file_name = file_name + ".xanalysis"
        method_call = {
            "method": "resumeAnalysis",
            "fileName": file_name
        }
        self._ref_session.run(method_call)

    def get_root_object(self):
        """
        [Beta] retrieve the root object

        :return: the root object
        :rtype: XObject
        """
        root_object_name = self._ref_session.__xplain_session__['focusObject'][
            'objectName']
        return XObject(root_object_name, self._ref_session)
        pass

    def get_xobject(self, object_name):
        """
        [Beta] retrieve the object with given name

        :return: the object with given name
        :rtype: XObject
        """
        object_found = self._ref_session.get_object_info(object_name)
        if object_found is not None:
            return XObject(object_found["objectName"], self._ref_session)
        else:
            return None

    def get_object_info(self, object_name):
        return self._ref_session.get_object_info(object_name)

    def get_dimension_info(self, object_name, dimension_name):
        return self._ref_session.get_dimension_info(object_name, dimension_name)

    def get_attribute_info(self, object_name, dimension_name, attribute_name):
        """
        find and retrieves the details of an attribute

        :param object_name: the name of xobject
        :param dimension_name: the name of dimension
        :param attribute_name: the name of attribute
        :return: details of this attribute in json format
        """

        return self._ref_session.get_attribute_info(object_name,
                                                    dimension_name,
                                                    attribute_name)

    def open_attribute(self, object_name, dimension_name, attribute_name,
                       request_name='',
                       data_frame=True):
        """
        convinient method to open an attribute

        :param object_name: name of object
        :type object_name: string
        :param dimension_name: name of dimension
        :type dimension_name: string
        :param attribute_name: name of attribute
        :type attribute_name: string
        :param request_name: id or name of request
        :type request_name: string
        :param data_frame: if result shall be returned as pandas
        :type data_frame: boolean
        :return: attribute groupped by on first level and aggregated by count.
        :rtype: attribute: data frame or json

        Example:
            >>> session = xplain.Xsession(url="myhost:8080", user="myUser",
            password="myPwd")
            >>> session.startup("mystartup")
            >>> session.open_attribute("Patient", "Age", "Agegroup")
        """

        if request_name == '':
            request_id = str(uuid.uuid4())
            method = {
                "method": "openAttribute",
                "object": object_name,
                "dimension": dimension_name,
                "attribute": attribute_name,
                "requestName": request_id

            }
        else:
            request_id = request_name
            method = {
                "method": "openAttribute",
                "object": object_name,
                "dimension": dimension_name,
                "attribute": attribute_name,
                "requestName": request_id
            }
        self._ref_session.run(method)
        return self._ref_session.get_result(request_id, data_frame)

    # def get_selected_instances(self, object_name, max_number,
    # data_frame=True):
    #     """
    #     display the instance details of selected objects
    #
    #     :param object_name: the name of selected Xobject
    #     :type object_name: string
    #     :param max_number: the maximal number of instances to be retrieved
    #     :type max_number: int
    #     :param data_frame: if the results shall be returned as pandas data
    #     frame
    #     :type data_frame: bool
    #     :return: list of instance details
    #     :rtype: pandas data frame or json
    #     """
    #     req = {
    #         "method": "getSelectedInstances",
    #         "maxNumberInstances": max_number,
    #         "elements": [{
    #             "object": object_name
    #         }]
    #     }
    #     result = self._ref_session.perform(req)
    #     if result.get("objectInstances") is not None:
    #         if data_frame:
    #             return pd.json_normalize(result.get("objectInstances"))
    #         else:
    #             return result.get("objectInstances")

    def get_variable_details(self, model_name, data_frame=True):
        """
        get the predictive model independent variables details

        :param model_name: the name of predictive model
        :type model_name: string
        :param data_frame: if result shall be returned as pandas
        :type data_frame: boolean
        :return: the model result
        :rtype: data frame or json
        """
        result = None

        if self._ref_session.get_session().get(
                'predictiveModels') is not None and \
                self._ref_session.get_session()["predictiveModels"].get(
                    model_name) is not None:
            result = self._ref_session.get_session()["predictiveModels"][
                model_name]['independentVariables']
            if data_frame:
                return pd.json_normalize(result)

        return result

    def refresh(self):
        """
        synchronize the session content with the backend

        """
        self._ref_session.refresh()

    def get_model_names(self):
        """
        list all loaded predictive models

        :return: list of model names
        :rtype: array of string
        """
        return self._ref_session.get_model_names()

    def get_variable_list(self, model_name):
        """
        get the list of independent variables of given predictive model

        :param model_name: name of predictive model
        :type model_name: string
        :return: list of independent variables
        :rtype: array of string
        """
        return self._ref_session.get_variable_list(model_name)

    def build_predictive_model(self, model_name, xmodel_config,
                               model_object_name, significance,
                               target_event_object_name,
                               target_selection_object_name,
                               target_selection_dimension_name,
                               target_selection_attribute,
                               output_prefix = None):
        """
        build predictive model [BETA!!]

        :param model_name: model name
        :type model_name: string
        :param xmodel_config: xmodel configuration file
        :type xmodel_config: string
        :param model_object_name: model object name
        :type model_object_name: string
        :param significance: significance 0.0 - 1.0
        :type significance: float
        :param target_event_object_name: target even object name
        :type target_event_object_name: string
        :param target_selection_object_name: target selection object name
        :type target_selection_object_name: string
        :param target_selection_dimension_name: target selection dimension name
        :type target_selection_dimension_name: string
        :param target_selection_attribute: target selection attribute name
        :type target_selection_attribute: string
        :param output_prefix: prefix of output csv files on file system,
        default is empty
        :type output_prefix: string
        :return: results of predictive model as dictionary of
        padas dataframes which includs independent varialbes,
        observations, learning log,
        predicted probabilities, ROC
        :rtype: dictionary

        Example:
            >>> xsession.build_predictive_model(model_name='Depression',
                                xmodel_config='DEPRESSION - demo.xmodel',
                                model_object_name='Person',
                                significance=0.9,
                                target_event_object_name='Diagnosen',
                                target_selection_object_name='Diagnosen',
                                target_selection_dimension_name='Type',
                                target_selection_attribute='Type')

        """
        return self._ref_session.build_predictive_model(
            model_name, xmodel_config, model_object_name, significance,
            target_event_object_name, target_selection_object_name,
            target_selection_dimension_name, target_selection_attribute,
            output_prefix
        )

    def get_selections(self):
        """
        display all global selections in the current xplain session

        :return: selections as json
        :rtype: list of json
        """
        return self._ref_session.get_selections()

    def get_instance_as_dataframe(self, elements):
        """
        get a pandas dataframe representation of the xplain artifacts
        references by elements,
        equivalent to the standard csv download functionality in XOE

        :param elements: array of x-element paths, each one referring a
        Xplain artifact, an object,
        a dimension or an attribute
        :type elements: list
        :return: Dataframe representation of requested instance
        :rtype: pd.Dataframe

        Example:
                elements: [
                 {"object": "Person"},
                 {"object": "Diagnosis", "dimension": "Physician"},
                 {"object": "Prescription", "dimension": "Rx Code",
                 "attribute": "ATC Hierarchy"},
                 {"object": "Prescription", "dimension": "Rx Code",
                 "attribute": "Substance"}
                ],

        """
        filename = "Flat Table Export.csv"
        self.run({
            "method": "saveAsCSV",
            "elements": elements,
        })
        response = self._ref_session.post_file_download(file_name=filename,
                                                        file_type="EXPORT_CSV"
                                                        )
        if response.ok:
            open(filename, 'wb').write(response.content)
            dataframe = pd.read_csv(filename, sep=';')
            os.remove(filename)
            return dataframe
        else:
            logging.info(response.reason)
            return None

    def download_result(self, file_name, save_as):
        """
        download a file from result directory of server and save it to
        current local path

         :param file_name: file name in result directory
        :type file_name: string
        :param save_as: downloaded file save as local file
        :type save_as: string
        """
        self._ref_session.download_result(file_name, save_as)

    def upload2data(self, file_name):
        """
        upload the file from current local directory to data directory on
        server
        :param file_name: file
        :type file_name: string
        """
        self._ref_session.upload2data(file_name)

    def get_result(self, query_name, data_frame=True):
        """
        get the result of the query
        :param query_name: the name /id of the query
        :type query_name: string
        :return: Dataframe result of the query
        :rtype: pd.Dataframe or json
        """
        return self._ref_session.get_result(query_name=query_name,
                                            data_frame=data_frame)

    def set_default_broadcast(self, broadcast):
        """
        set default broadcast behaviour so that other xplain client sharing
        the same xplain session could get informed about the update of
        current xplain session.

        :param broadcast: after successful session update via python call,
        if a default
        refresh signal should be broadcasted to all xplain clients those are
        sharing the same xplain session, in order to force them to perform the
        refresh to get the most current session.
        :type broadcast: boolean

        """
        self._ref_session.set_default_broadcast(broadcast)

    def open_sequence(self, target_object=None,
                      base_object=None,
                      ranks=None,
                      reverse=False,
                      names=None,
                      name_postfixes=None,
                      dimensions_2_replicate=None,
                      sort_dimension=None,
                      zero_point_dimension=None,
                      selections=None,
                      selection_set_definition_rank=None,
                      floating_semantics=False,
                      attribute_2_copy=None,
                      sequence_name=None,
                      rank_dimension_name=None,
                      rank_zero_is_first_instance_equal_or_greater_zero_point=False,
                      transition_attribute=None,
                      transition_level=None,
                      open_marginal_queries=False,
                      open_transition_queries=True,
                      selection_set=None):
        self._ref_session.open_sequence(target_object,
                      base_object,
                      ranks, reverse, names, name_postfixes,
                      dimensions_2_replicate, sort_dimension,
                       zero_point_dimension,
                      selections,
                      selection_set_definition_rank,
                      floating_semantics, attribute_2_copy,
                      sequence_name, rank_dimension_name,
                      rank_zero_is_first_instance_equal_or_greater_zero_point,
                      transition_attribute, transition_level,
                      open_marginal_queries,
                      open_transition_queries,
                      selection_set)

    def get_open_sequences(self, sequence_name):
        return self._ref_session.get_open_sequences(sequence_name)


    def get_sequence_transition_matrix(self, sequence_name):
        return self._ref_session.get_sequence_transition_matrix(sequence_name)

    def gen_xtable(self, data, config, file_name):
        return self._ref_session.gen_xtable(data=data, xtable_config=config,
                                            file_name=file_name)

    def list_files(self, ownership, file_type, file_extension=None):
        return self._ref_session.list_files(ownership=ownership,
                                            file_type=file_type,
                                            file_extension=file_extension
                                            )

    def read_file(self, ownership, file_type, file_path):
        return self._ref_session.read_file(ownership=ownership,
                                           file_type=file_type,
                                           file_path=file_path
                                           )

    def validate_db(self, db_connection_config):
        self._ref_session.validate_db(db_connection_config=db_connection_config)

    def run_py(self, file_name, options="", ownership='PUBLIC'):
        return self._ref_session.run_py(file_name=file_name, options=options,
                                        ownership=ownership)

    def http_get(self, entrypoint, params=None):
        return self._ref_session.http_get(entrypoint=entrypoint, params=params)

    def http_post(self, entrypoint, payload):
        return self._ref_session.http_post(entrypoint=entrypoint, payloadJson=payload)


