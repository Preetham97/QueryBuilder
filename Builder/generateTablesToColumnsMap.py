# import dash
# import dash_bootstrap_components
import ast
import psycopg2
import pgConnect
import json

from collections import  defaultdict
def connectiontest(database,user,password,host,port):
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    try:
        # cursor.execute("INSERT INTO sbufhr.savedqueries (query_name, query_comments, query_string) VALUES(%s, %s, %s)",
        #                (queryName, comments, query_string))
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='sbufhr'")
        tables= [y[0] for y in cursor.fetchall()]

        hashmap = defaultdict(list)
        for table in tables:
            #columns = []
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'sbufhr' AND table_name="+"'"+table+"'")
            columns = [item[0] for item in cursor.fetchall()]
            hashmap[table] = columns

        print(hashmap)
        with open("tablesToColumns.json", "w") as outfile:
            json.dump(hashmap, outfile)

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("failure:", e)
        return '{"result":"failure"}'

def remove_id():
    result = {}
    with open('tablesToColumns.json') as f:
        data = json.load(f)
    for key,value in data.items():
        result[key] = []
        for column in value:
            if "id" in column or "_cd" in column or "code" in column or "_key" in column:
                continue
            else:
                result[key].append(column)
        result[key].sort()
    result["encounters"] = ["encntr_id", "person_id"] + result["encounters"]


    with open('tablesToColumns_1.json', 'w') as json_file:
        json.dump(result, json_file)

# with open('arguments.txt', 'r') as f:
#     args = ''
#     for line in f.readlines():
#         line = line.strip()
#         args += line
#     f.close()
#
# args = "".join(args).strip('\n')
# args_dict = ast.literal_eval(args)
#
# schema = args_dict['schema']
# db = pgConnect.db(schema)
#
# saveQueryResponseJson = connectiontest(database=args_dict['database'], user=args_dict['user'],
#                             password=args_dict['password'], host=args_dict['host'], port=args_dict['port'])

remove_id()


