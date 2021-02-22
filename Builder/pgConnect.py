import json

import psycopg2
import dicts

filters = []

class db():
    dictionaries = dicts.dicts()

    refer = dictionaries.refer
    operator_dict_int = dictionaries.operator_dict_int
    operator_dict_str = dictionaries.operator_dict_str
    dict_no_encntr = dictionaries.dict_no_encntr
    attr_no_enc = dictionaries.attr_no_enc
    fields = dictionaries.fields
    attributes = dictionaries.attributes
    attr_list = dictionaries.attr_list

    schema = ''

    tables = []
    tables_no_encntr = []
    columns = []

    sql_query = ''

    def __init__(self, schema):
        self.schema = schema
        self.columns = ['encounters.encntr_id']
        self.tables = []
        self.tables_no_encntr = []
        self.sql_query = ''


        fileds_removed = []
        for field in self.fields:
            if "id" in field or "_cd" in field or "code" in field or "_key" in field or "dt_" in field:
                continue
            fileds_removed.append(field)
        fileds_removed.sort()
        self.fields = fileds_removed


    def parse_json(self, condition, rules):

        query_condition = ''

        for rule in rules:
            if 'condition' in rule:
                group = self.parse_json(rule['condition'], rule['rules'])
                if group == '':
                    continue
                query_condition = query_condition + '( ' + group + ' )' + ' ' + condition + ' '
            else:
                if rule['id'] == 'empty':
                    continue
                field = rule['field']
                operator = rule['operator']
                value = rule['value']
                value_type = rule['type']

                '''Collect fields for select statement'''
                if field in self.refer:
                    column = self.refer[field]
                else:
                    column = field

                if column not in self.columns:
                    self.columns.append(column)

                '''Parse operator + value for where statement'''
                if value_type == 'integer':
                    if value == None:
                        value = ''

                    if operator in ['between', 'not_between']:
                        value = value[0] + ' AND ' + value[1]

                    where_condition = self.operator_dict_int[operator] + value

                elif value_type == 'string':
                    if operator in ["in", "not_in"]:
                        set_in = "("
                        for ele in value.split(','):
                            set_in += "'{}',".format(ele)
                        set_in = set_in[:-1] + ")"

                        where_condition = self.operator_dict_str[operator] + set_in
                    else:
                        where_condition = self.operator_dict_str[operator].format(value)

                elif value_type == 'date':
                    if operator in ['between', 'not_between']:
                        value = value[0] + "'" + ' AND ' + "'" + value[1]
                    value = "'" + value.replace('/', '-') + "'"
                    where_condition = self.operator_dict_int[operator] + value

                query_condition = query_condition + column + where_condition + ' ' + condition + ' '

        query_condition = query_condition[:-4]

        return query_condition

    def parse(self, rules_json, sel_fields=[]):
        condition = rules_json['condition']
        rules = rules_json['rules']
        query_condition = self.parse_json(condition, rules)

        '''Query 'select' part '''
        if sel_fields:
            query_sel = 'select '
            for i in range(len(sel_fields)):
                column = sel_fields[i]
                if i==0:
                    # query_sel = 'select distinct(encounters.encntr_id),'
                    query_sel = query_sel + 'distinct({}),'.format(column)
                else:
                    query_sel = query_sel + column + ','
        else:
            query_sel = 'select distinct(encounters.encntr_id),encounters.person_id,'
            colunm_added = set()
            for column in self.columns:
                if column == 'encounters.encntr_id' or column == 'encounters.person_id':
                    continue
                else:
                    if column not in colunm_added:
                        query_sel = query_sel + column.split('.')[0] + '.*' + ','
                        colunm_added.add(column)

        query_sel = query_sel[:-1] + ' '

        '''Query 'join & on' part'''
        for column in self.columns:
            table = column.split('.')[0]
            while table not in self.tables:
                if table in self.dict_no_encntr:
                    if table not in self.tables_no_encntr:
                        self.tables_no_encntr.append(table)
                    table = self.dict_no_encntr[table]
                    continue
                self.tables.append(table)

        join_on = []
        for table in self.tables:
            if table == 'labevents':
                join_on.append("labevents.encounter_id")
            else:
                join_on.append(table + "." + "encntr_id")

        if len(self.columns) == 1:
            query_join = 'from ' + self.schema + '.' + self.columns[0].split('.')[0] + ' '
        else:
            query_join = 'from ' + self.schema + '.' + self.tables[0] + ' '

            for i in range(1, len(self.tables)):
                query_join = query_join + 'join ' + self.schema + '.' + self.tables[i] + ' on ' + join_on[i] + ' = ' + \
                         join_on[0] + ' '

            for table_no in self.tables_no_encntr:
                join_on_list = self.attr_no_enc[table_no]
                query_join = query_join + 'join ' + self.schema + '.' + table_no + ' on ' + join_on_list[0] + ' = ' + \
                         join_on_list[1] + ' '

        '''Query 'where' part'''
        query_where = 'where ' + query_condition

        '''Combine three parts'''
        self.sql_query = query_sel + query_join + query_where + ';'

        return self.sql_query

    def get_data(self, rules_json, database, user, password, host, port):

        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

        cursor = conn.cursor()

        rules = rules_json['rules']
        print("rules",rules)
        if "quick" in rules_json:
            quick = rules_json['quick']
        else:
            quick = False

        if "interest-fields" in rules_json:
            select_fields = rules_json["interest-fields"]
        else:
            select_fields = []

        self.parse(rules,select_fields)
        print("SQL_QUERY:", self.sql_query)
        print()

        cursor.execute(self.sql_query)

        header = [cursor.description[i].name for i in range(len(cursor.description))]

        if quick:
            data = cursor.fetchmany(50)
        else:
            data = cursor.fetchall()

        data_json = self.data_to_json(data, header)

        data_with_sql = {"sql":self.sql_query,"data_json":data_json}
        data_json = json.dumps(data_with_sql)

        conn.commit()
        cursor.close()
        conn.close()

        return data_json

    def data_to_json(self, data, header, keep_id=False):
        jsonData = []

        for row in data:
            row_json = {}
            for i in range(len(header)):
                if keep_id == False:
                    # if "id" in header[i] and header[i] not in ["encntr_id", "person_id"]:
                    #     continue
                    if ("id" in header[i] or "_cd" in header[i] or "code" in header[i] or "_key" in header[i]) and header[i] not in ["encntr_id", "person_id"]:
                        continue
                row_json[header[i]] = str(row[i])
            jsonData.append(row_json)


        jsonData = json.dumps(jsonData)

        return jsonData

    def saveQuery(self,saveQueryJson, database, user, password, host, port):
        queryName = saveQueryJson['queryName']
        comments = saveQueryJson['comments']
        query_string = saveQueryJson['queryJsonString']

        # insert into savedqueries table
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        #insertQueryString = self.generateInsertQuery(queryName,comments,query_string)
        #print("Insert Query String:", insertQueryString)
        try:
            cursor.execute("INSERT INTO sbufhr.savedqueries (query_name, query_comments, query_string) VALUES(%s, %s, %s)", (queryName, comments, query_string))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print("failure:",e)
            return '{"result":"failure"}'

        return '{"result":"success"}'

    def generateInsertQuery(self, queryName, comments, query_string):

        queryString = 'insert into ' + self.schema+'.savedqueries' + '(query_name,query_comments,query_string)'
        queryString = queryString + ' values(' + +queryName+ + ',' + comments + ',' + queryName + ')'
        return queryString + ';'

    def selectQuery(self, database, user, password, host, port):
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM sbufhr.savedqueries;")
            header = [cursor.description[i].name for i in range(len(cursor.description))]

            # data = cursor.fetchmany(50)
            data = cursor.fetchall()

            data_json = self.data_to_json(data, header)

            conn.commit()
            cursor.close()
            conn.close()

            return data_json
        except Exception as e:
            print("failure:", e)
            return

    def search(self, search_field,researchKeywors, rules,database, user, password, host, port):

        if len(researchKeywors.strip())==0:
            return []

        try:
            filters = []
            return_data = []

            # -------------Non-dt tables--------------#

            researchValue_list = researchKeywors.split(',')

            if search_field:

                for researchValue in researchValue_list:
                    researchValue.strip()
                    researchValue="_".join(researchValue.split())

                    for field in self.fields:
                        if researchValue in field:
                            return_data.append(field)

            else:
                # corresponding_value_fields={}

                conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
                cursor = conn.cursor()

                for researchValue in researchValue_list:
                    # corresponding_value_fields[researchValue]=[]
                    researchValue.strip()

                    searchQuery = "SELECT result.attr_id FROM (SELECT keywords.attr_id FROM sbufhr.keywords WHERE keywords.keywords LIKE '%{}%') AS result Group by result.attr_id;".format(
                        str(researchValue))

                    cursor.execute(searchQuery)
                    header = [cursor.description[i].name for i in range(len(cursor.description))]
                    data = cursor.fetchall()
                    data_json = self.data_to_json(data, header, keep_id=True)

                    jdata = json.loads(data_json)
                    if len(jdata) != 0:
                        for d in jdata:
                            field = self.attr_list[int(d['attr_id'])]
                            filter = {"id": field, "field": field, "type": "string", "input": "text", "operator": "contains",
                                      "value": str(researchValue)}
                            filters.append(filter)

                            field_value = "{}\xa0=\xa0{}".format(field,str(researchValue))
                            return_data.append(field_value)

                    # -------------Non-dt tables--------------#

                    for field in self.attributes:
                        # print('attr_passed',attr)
                        table_name = 'sbufhr.' + field.split(".")[0]
                        searchQuery = "SELECT {} FROM {} WHERE {} LIKE '%{}%';".format(field, table_name, field,
                                                                                       str(researchValue))

                        cursor.execute(searchQuery)
                        header = [cursor.description[i].name for i in range(len(cursor.description))]
                        data = cursor.fetchmany(1)
                        data_json = self.data_to_json(data, header)

                        check = data_json[1:-1]
                        if check:
                            filter = {"id": field, "field": field, "type": "string", "input": "text", "operator": "contains",
                                      "value": str(researchValue)}
                            filters.append(filter)
                            # corresponding_value_fields[researchValue].append(field)

                            field_value = "{}\xa0=\xa0{}".format(field, str(researchValue))
                            return_data.append(field_value)


                # return_data['return_fields'].append(corresponding_value_fields)

                conn.commit()
                cursor.close()
                conn.close()

            return_fields = json.dumps(return_data)
            return return_fields

        except Exception as e:
            print("failure:", e)
            return '{"result":"failure"}'

    def setRules(self,rules,filters):
        condition = rules['condition']
        rule = rules['rules'][-1]
        if 'condition' in rule:
            group_rules = [self.setRules(rule,filters)]
            rule_rt = rules['rules'][:-1]+group_rules
            rule_rt = {'condition':condition,'rules':rule_rt}
        else:
            if rule["id"] == "empty":
                rule_rt = rules['rules'][:-1] + filters
                rule_rt = {'condition': condition, 'rules': rule_rt}
            else:
                rule_rt = rules['rules'] + filters
                rule_rt = {'condition': condition, 'rules': rule_rt}

        return rule_rt

    def rule_setter(self,is_search_fields, fields_select, rules):
        filters = []
        if is_search_fields:
            for field in fields_select:
                filter = {"id": field, "field": field, "type": "string", "input": "text",
                              "operator": "is_not_null",
                              "value": None}
                filters.append(filter)
        else:
            for field in fields_select:
                field.strip()
                print(field.split('\xa0=\xa0'))
                filter_id = field.split('\xa0=\xa0')[0]
                filter_value = field.split('\xa0=\xa0')[1]
                filter = {"id": filter_id, "field": filter_id, "type": "string", "input": "text", "operator": "contains",
                                      "value": filter_value}
                filters.append(filter)
        set_rules = self.setRules(rules, filters)
        set_rules = json.dumps(set_rules)
        return set_rules

    def getLabData(self, para,database, user, password, host, port):
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        try:
            if para["tab_id"] == "encounters":
                sql_query = "select distinct(encounters.encntr_id),encounters.reg_dt_tm " \
                            "from sbufhr.encounters " \
                            "where encounters.person_id = {} ORDER BY encounters.reg_dt_tm;".format(para["patientId"])
            elif para["encntrId"] != "":
                sql_query = "select distinct(encounters.encntr_id),encounters.person_id,{}.* " \
                            "from sbufhr.encounters join sbufhr.{} on {}.encntr_id = encounters.encntr_id " \
                            "where encounters.person_id = {} and encounters.encntr_id = {};".format(para["tab_id"], para["tab_id"], para["tab_id"],
                                                                      para["patientId"],para["encntrId"])
            else:
                sql_query = "select distinct(encounters.encntr_id),encounters.person_id,{}.* " \
                        "from sbufhr.encounters join sbufhr.{} on {}.encntr_id = encounters.encntr_id " \
                        "where encounters.person_id = {};".format(para["tab_id"],para["tab_id"],para["tab_id"],para["patientId"])
            print("sql_query",sql_query)
            cursor.execute(sql_query)
            header = [cursor.description[i].name for i in range(len(cursor.description))]

            data = cursor.fetchall()
            data_json = self.data_to_json(data, header)

            # data_with_sql = {"sql": self.sql_query, "data_json": data_json}
            data_json = json.dumps(data_json)

            conn.commit()
            cursor.close()
            conn.close()

            return data_json
        except Exception as e:
            print("failure:", e)
            return

    def getId(self, para,database, user, password, host, port):
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        try:
            if para["data_name"] == "birth_dt":
                sql_query = "select distinct(encounters.person_id) " \
                            "from sbufhr.encounters " \
                            "where encounters.birth_dt between '{}' and '{}';".format(para["startdate"],para["enddate"])
            elif para["data_name"] == "reg_dt_tm":
                sql_query = "select distinct(encounters.encntr_id) " \
                            "from sbufhr.encounters  " \
                            "where encounters.reg_dt_tm between '{}' and '{}' and encounters.person_id = {};".format(para["startdate"],para["enddate"],para["patientId"])

            print("sql_query",sql_query)
            cursor.execute(sql_query)
            header = [cursor.description[i].name for i in range(len(cursor.description))]

            data = cursor.fetchall()
            data_json = self.data_to_json(data, header)

            # data_with_sql = {"sql": self.sql_query, "data_json": data_json}
            data_json = json.dumps(data_json)

            conn.commit()
            cursor.close()
            conn.close()

            return data_json
        except Exception as e:
            print("failure:", e)
            return