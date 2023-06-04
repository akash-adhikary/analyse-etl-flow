#!/usr/bin/python
import os
import re
import sys
import base64
import zlib


dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir=f"{dir_path}{os.sep }etl_flow"
input_dir=f"{dir_path}{os.sep }sql"

def visualizeFlow(tableName):
    tablesProcessed=[]
    tables2beProcessed=tableName.copy()
    mermaidData=exploreFlow(tables2beProcessed,tablesProcessed,"graph RL;\n")
    print(mermaidData)
    korkiLink="https://kroki.io/mermaid/svg/"+base64.urlsafe_b64encode(zlib.compress(mermaidData.encode('utf-8'), 9)).decode('ascii')
    print(korkiLink)
    outF = open(f"{output_dir}{os.sep }{tableName[0]}_ETL_FLOW.md", "w") 
    mermaidfile=f"""# Mermaid Js Diagram for {tableName[0]}\n```mermaid\n{mermaidData}\n```\n# Mermaid Js Link (Open Via Browser)\n[Mermaid JS API]({korkiLink})"""
    outF.write(mermaidfile)
    outF.close()

def exploreFlow(tables2beProcessed,tablesProcessed,mermaidContent):
    for table in tables2beProcessed:
        if table not in tablesProcessed:
            metalist=sqlLst(table)
            for meta in metalist:
                print(meta['targetTable'])
                print(meta['sqlName'])
                print(meta['dependencies'])
                mermaidContent+=f"{meta['sqlName']} -->{meta['targetTable']};\n"
                for tab in meta['dependencies']:
                    mermaidContent+=f"{tab} -->{meta['sqlName']}:::sqlClass;\n"
                tables2beProcessed.extend(meta['dependencies'])
                tables2beProcessed=list(set(tables2beProcessed))
            tables2beProcessed.remove(table)
            tablesProcessed.append(table)

    if(len(tables2beProcessed)>0):
        return(exploreFlow(tables2beProcessed,tablesProcessed,mermaidContent))
    else:
        return(f"{mermaidContent}classDef sqlClass fill:#f96;")
    
    

def sqlLst(tableName):
    ls = os.listdir(input_dir)
    searchString=f"INSERT INTO {tableName}"
    sql_list  = []
    for fname in ls:
        if os.path.isfile(input_dir + os.sep + fname) and fname.endswith('.sql'):
            with open(input_dir + os.sep + fname, 'r') as file:
                content = file.read()
                if searchString in content:
                   meta={'sqlName':fname,'targetTable':tableName,'dependencies':processSQL(content)}
                   sql_list.append(meta)
    return(sql_list) 

def processSQL(content):
    tables = re.findall("FROM\s*\S*\s", content)
    tables.extend(re.findall("JOIN\s*\S*\s", content))
    dependencies=[]
    if tables:
        for table in tables:
            dependencies.append(table.replace("FROM","").replace("JOIN","").replace(" ",""))
    else:
        print("No match")
    if '(\n' in dependencies:
        dependencies.remove('(\n')
    return(list(set(dependencies)))

visualizeFlow(['EMPLOYEE'])





