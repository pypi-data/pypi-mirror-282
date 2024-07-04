from dataclasses import dataclass
import json
from mysql.connector import Error
import mysql.connector
import mysql
import numpy as np
from typing import Final
import time

TABLE_1FIELD_NAME:Final = "id_RUN"
TABLE_2FIELD_NAME:Final = "ACSN"
TABLE_3FIELD_NAME:Final = "Date_Time"
TABLE_4FIELD_NAME:Final = "Thresholds_X_JSON"
TABLE_5FIELD_NAME:Final = "Thresholds_Y_JSON"
TABLE_6FIELD_NAME:Final = "TimeSlice_B1"
TABLE_7FIELD_NAME:Final = "Delay_B1"
TABLE_8FIELD_NAME:Final = "TimeSlice_B2"
TABLE_9FIELD_NAME:Final = "Delay_B2"
TABLE_10FIELD_NAME:Final = "DATA_X1_JSON"
TABLE_11FIELD_NAME:Final = "DATA_Y1_JSON"
TABLE_12FIELD_NAME:Final = "DATA_X2_JSON"
TABLE_13FIELD_NAME:Final = "DATA_Y2_JSON"
TABLE_14FIELD_NAME:Final = "Thresholds_GS_JSON"
TABLE_15FIELD_NAME:Final = "DATA_GS1_JSON"
TABLE_16FIELD_NAME:Final = "DATA_GS2_JSON"

@dataclass
class DownloadData:
    id:int
    acsn:int
    dateTime:str
    delay:float
    timeslice:float
    threshold: np.ndarray
    matrix:np.ndarray

@dataclass
class ParametersConnection:
    user: str = ""
    password: str = ""
    host: str = ""
    database: str = ""
    table: str = ""
    port: int = 0
    
    def getConfig(self):
        return {
            'user': self.user,
            'password': self.password,
            'host': self.host,
            'database': self.database,
            'port': self.port,
            'raise_on_warnings': True,
            'connection_timeout':3
            }
#@debugMode.conditionalDebugDecorator(timeout(dec_timeout=4, timeout_exception=TimeoutError))
def openConnection(parameters):
    config = parameters.getConfig()
    return mysql.connector.connect(**config)

def getRecordsInfoByFilterID(table,connector,fromId,toId):
    query = "SELECT {0},{1},{2},{3},{4},{5} FROM {6} WHERE {7} BETWEEN {8} AND {9}".format(
        TABLE_1FIELD_NAME, #id_Run
        TABLE_3FIELD_NAME, #DateTime
        TABLE_6FIELD_NAME, #TimeSliceB1
        TABLE_7FIELD_NAME, #DelayB1
        TABLE_8FIELD_NAME, #TimeSliceB2
        TABLE_9FIELD_NAME, #DelayB2
        table,
        TABLE_1FIELD_NAME,
        fromId,
        toId
    )
    return __executeQueryInfoLoad__(query,connector)

def getRecordsInfoByDateTime(table,connector,fromDateTime,toDateTime):
    query = "SELECT {0},{1},{2},{3},{4},{5} FROM {6} WHERE {7} BETWEEN '{8}' AND '{9}'".format(
        TABLE_1FIELD_NAME, #id_Run
        TABLE_3FIELD_NAME, #DateTime
        TABLE_6FIELD_NAME, #TimeSliceB1
        TABLE_7FIELD_NAME, #DelayB1
        TABLE_8FIELD_NAME, #TimeSliceB2
        TABLE_9FIELD_NAME, #DelayB2
        table,
        TABLE_3FIELD_NAME,
        fromDateTime,
        toDateTime
    )
    return __executeQueryInfoLoad__(query,connector)

def getRecordsInfoByAll(table,connector):
    query = "SELECT {0},{1},{2},{3},{4},{5} FROM {6}".format(
        TABLE_1FIELD_NAME, #id_Run
        TABLE_3FIELD_NAME, #DateTime
        TABLE_6FIELD_NAME, #TimeSliceB1
        TABLE_7FIELD_NAME, #DelayB1
        TABLE_8FIELD_NAME, #TimeSliceB2
        TABLE_9FIELD_NAME, #DelayB2
        table
    )
    return __executeQueryInfoLoad__(query,connector)

def getRecordsInfoByFilterIDByParameters(parameters,fromId,toId):
    with openConnection(parameters) as connector:
        query = "SELECT {0},{1},{2},{3},{4},{5} FROM {6} WHERE {7} BETWEEN {8} AND {9}".format(
            TABLE_1FIELD_NAME, #id_Run
            TABLE_3FIELD_NAME, #DateTime
            TABLE_6FIELD_NAME, #TimeSliceB1
            TABLE_7FIELD_NAME, #DelayB1
            TABLE_8FIELD_NAME, #TimeSliceB2
            TABLE_9FIELD_NAME, #DelayB2
            parameters.table,
            TABLE_1FIELD_NAME,
            fromId,
            toId
        )
        return __executeQueryInfoLoad__(query,connector)

def getRecordsInfoByDateTimeByParameters(parameters,fromDateTime,toDateTime):
    with openConnection(parameters) as connector:
        query = "SELECT {0},{1},{2},{3},{4},{5} FROM {6} WHERE {7} BETWEEN '{8}' AND '{9}'".format(
            TABLE_1FIELD_NAME, #id_Run
            TABLE_3FIELD_NAME, #DateTime
            TABLE_6FIELD_NAME, #TimeSliceB1
            TABLE_7FIELD_NAME, #DelayB1
            TABLE_8FIELD_NAME, #TimeSliceB2
            TABLE_9FIELD_NAME, #DelayB2
            parameters.table,
            TABLE_3FIELD_NAME,
            fromDateTime,
            toDateTime
        )
        return __executeQueryInfoLoad__(query,connector)

def getRecordsInfoByAllByParameters(parameters):
    with openConnection(parameters) as connector:
        query = "SELECT {0},{1},{2},{3},{4},{5} FROM {6}".format(
            TABLE_1FIELD_NAME, #id_Run
            TABLE_3FIELD_NAME, #DateTime
            TABLE_6FIELD_NAME, #TimeSliceB1
            TABLE_7FIELD_NAME, #DelayB1
            TABLE_8FIELD_NAME, #TimeSliceB2
            TABLE_9FIELD_NAME, #DelayB2
            parameters.table
        )
        return __executeQueryInfoLoad__(query,connector)

def __executeQueryInfoLoad__(query,connector):
    with connector.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            resultList = list()
            for item in result:
                resultList.append({
                    'id_Run':item[0],
                    'DateTime':item[1],
                    'TimeSliceB1':item[2],
                    'DelayB1':item[3],
                    'TimeSliceB2':item[4],
                    'DelayB2':item[5]})
            return resultList
        except Error as e:
            print("Error while connecting to MySQL:")

def getRecordByIdFirstBank(table, connector, id):
    query = "SELECT {0},{1},{2},{3},{4},{5},{6} FROM {7} WHERE {8}={9}".format(
        TABLE_1FIELD_NAME,
        TABLE_3FIELD_NAME,
        TABLE_6FIELD_NAME,
        TABLE_7FIELD_NAME,
        TABLE_10FIELD_NAME,
        TABLE_11FIELD_NAME,
        TABLE_15FIELD_NAME,
        table,
        TABLE_1FIELD_NAME,
        str(id))
    with connector.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return __getDataBySTR__(result[0])  
        except Error as e:
            print("Error while connecting to MySQL:")

def getRecordByIdListFirstBank(table, connector, idList):
    query = "SELECT {0},{1},{2},{3},{4},{5},{6} FROM {7} WHERE {8}={9}".format(
        TABLE_1FIELD_NAME,
        TABLE_3FIELD_NAME,
        TABLE_6FIELD_NAME,
        TABLE_7FIELD_NAME,
        TABLE_10FIELD_NAME,
        TABLE_11FIELD_NAME,
        TABLE_15FIELD_NAME,
        table,
        TABLE_1FIELD_NAME,
        str(idList[0]))
    for i in range(1,np.size(idList)):
        query += " OR {0}={1}".format(TABLE_1FIELD_NAME,idList[i])
    with connector.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            resutlList = list()
            for item in result:
                resutlList.append(__getDataBySTR__(item))
            return resutlList
        except Error as e:
            print("Error while connecting to MySQL:")

def getRecordByIdSecondBank(table, connector, id):
    query = "SELECT {0},{1},{2},{3},{4},{5},{6} FROM {7} WHERE {8}={9}".format(
        TABLE_1FIELD_NAME,
        TABLE_3FIELD_NAME,
        TABLE_8FIELD_NAME,
        TABLE_9FIELD_NAME,
        TABLE_12FIELD_NAME,
        TABLE_13FIELD_NAME,
        TABLE_16FIELD_NAME,
        table,
        TABLE_1FIELD_NAME,
        str(id))
    with connector.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return __getDataBySTR__(result[0])  
        except Error as e:
            print("Error while connecting to MySQL:")

def getRecordByIdListSecondBank(table, connector, idList):
    query = "SELECT {0},{1},{2},{3},{4},{5},{6} FROM {7} WHERE {8}={9}".format(
        TABLE_1FIELD_NAME,
        TABLE_3FIELD_NAME,
        TABLE_8FIELD_NAME,
        TABLE_9FIELD_NAME,
        TABLE_12FIELD_NAME,
        TABLE_13FIELD_NAME,
        TABLE_16FIELD_NAME,
        table,
        TABLE_1FIELD_NAME,
        str(idList[0]))
    for i in range(1,np.size(idList)):
        query += " OR {0}={1}".format(TABLE_1FIELD_NAME,idList[i])
    with connector.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            resutlList = list()
            for item in result:
                resutlList.append(__getDataBySTR__(item))
            return resutlList
        except Error as e:
            print("Error while connecting to MySQL:")

'''def __getDataBySTR__(str):
    listMatrixX=json.loads(str[3])
    listMatrixY=json.loads(str[4])
    resultArray = np.zeros(shape=(len(listMatrixX),len(listMatrixX[0])+len(listMatrixY[0])),dtype=int)
    for i in range(0,len(listMatrixX)):
        for j in range(0,len(listMatrixX[0])):
            resultArray[i][j] = listMatrixX[i][j]
    for i in range(0,len(listMatrixY)):
        for j in range(len(listMatrixX[0]),len(listMatrixX[0])+len(listMatrixY[0])):
            resultArray[i][j] = listMatrixY[i][j-len(listMatrixX[0])]
    return DownloadData(
        id=id,
        acsn=0,
        threshold=None,
        dateTime=str[0],
        delay=str[2],
        timeslice=str[1],
        matrix=resultArray
        ) '''
def __getDataBySTR__(str):
    listMatrixX=json.loads(str[4])
    listMatrixY=json.loads(str[5])
    listAdditionalCounter = json.loads(str[6])
    resultArray = np.zeros(shape=(len(listMatrixX),len(listMatrixX[0])+len(listMatrixY[0]) + len(listAdditionalCounter[0])),dtype=int)
    for i in range(0,len(listMatrixX)):
        for j in range(0,len(listMatrixX[0])):
            resultArray[i][j] = listMatrixX[i][j]
    for i in range(0,len(listMatrixY)):
        for j in range(len(listMatrixX[0]),len(listMatrixX[0])+len(listMatrixY[0])):
            resultArray[i][j] = listMatrixY[i][j-len(listMatrixX[0])]
    size = len(listMatrixX[0])+len(listMatrixY[0])
    lenBefore = len(listMatrixX[0])+len(listMatrixY[0])
    for i in range(len(listAdditionalCounter)):
        for j in range (len(listAdditionalCounter[0])):
            resultArray[i][lenBefore + j] = listAdditionalCounter[i][j]
    return DownloadData(
        id=int(str[0]),
        acsn=0,
        threshold=None,
        dateTime=str[1],
        delay=str[3],
        timeslice=str[2],
        matrix=resultArray
        ) 
def __getRecordByIdSTR__(connector,query):
    with connector.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            listMatrixX=json.loads(result[0][3])
            listMatrixY=json.loads(result[0][4])
            resultArray = np.zeros(shape=(len(listMatrixX),len(listMatrixX[0])+len(listMatrixY[0])),dtype=int)
            for i in range(0,len(listMatrixX)):
                for j in range(0,len(listMatrixX[0])):
                    resultArray[i][j] = listMatrixX[i][j]
            for i in range(0,len(listMatrixY)):
                for j in range(len(listMatrixX[0]),len(listMatrixX[0])+len(listMatrixY[0])):
                    resultArray[i][j] = listMatrixY[i][j-len(listMatrixX[0])]
            return DownloadData(
                id=id,
                acsn=0,
                threshold=None,
                dateTime=result[0][0],
                delay=result[0][2],
                timeslice=result[0][1],
                matrix=resultArray
                )            
        except Error as e:
            print("Error while connecting to MySQL:")
#@debugMode.conditionalDebugDecorator(timeout(dec_timeout=4, timeout_exception=TimeoutError))
def parametersIsValid(parameters):
    config = parameters.getConfig()
    with mysql.connector.connect(**config) as connector:
        #print(connector)
        return getCountRecords(parameters.table, connector) > 0

def getInfoFirstAndLastRecord(table, connector):
    count = getCountRecords(table, connector)
    firstRecord = getRecordByIdFirstBank(table, connector, 1)
    lastRecord = getRecordByIdFirstBank(table, connector, count)
    return{"firstDataTime":firstRecord.dateTime,"lastDataTime":lastRecord.dateTime,"count":count}

def getCountRecordsByParameters(sqlParameters):
    with openConnection(sqlParameters) as connector:
        return getCountRecords(sqlParameters.table, connector)
    
def getCountRecords(table, connector):
    cursor = connector.cursor()
    result = getCountRecordsByCursor(cursor, table)
    cursor.close()
    return result

def getCountRecordsByCursor(cursor, table):
    query = "SELECT COUNT(*) FROM {0}".format(table)
    #print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    #print("Count:",result[0][0])
    return result[0][0]

def getCursorWODataByParameters(parameters):
    strQuery = ("SELECT {0}, {1}, {2}, {3}, {4}, {5}, {6} FROM {7}".format(
        TABLE_1FIELD_NAME,
        TABLE_2FIELD_NAME,
        TABLE_3FIELD_NAME,
        TABLE_6FIELD_NAME,
        TABLE_7FIELD_NAME,
        TABLE_8FIELD_NAME,
        TABLE_9FIELD_NAME,
        parameters.table))

    try:
        connector = mysql.connector.connect(**(parameters.getConfig()))
        cursor = connector.cursor()
        cursor = mysql.cursors
        cursor.execute(strQuery)
        return (connector, cursor)
    except TimeoutError as e:
        print("TimeoutError while connecting to MySQL:".format(e))
    except TypeError as e:
        print("TypeError while connecting to MySQL:".format(e))
        
def getCursorWODataByConnector(parameters, connector):
    strQuery = ("SELECT {0}, {1}, {2}, {3}, {4}, {5}, {6} FROM {7}".format(
        TABLE_1FIELD_NAME,
        TABLE_2FIELD_NAME,
        TABLE_3FIELD_NAME,
        TABLE_6FIELD_NAME,
        TABLE_7FIELD_NAME,
        TABLE_8FIELD_NAME,
        TABLE_9FIELD_NAME,
        parameters.table))

    try:
        cursor = connector.cursor()
        cursor.execute(strQuery)
        return cursor
    except TimeoutError as e:
        print("TimeoutError while connecting to MySQL:".format(e))
    except TypeError as e:
        print("TypeError while connecting to MySQL:".format(e))
        
def getCursorIDDataByConnector(table, connector):
    strQuery = ("SELECT {0} FROM {1}".format(
        TABLE_1FIELD_NAME,
        table))

    try:
        cursor = connector.cursor()
        cursor.execute(strQuery)
        return cursor
    except TimeoutError as e:
        print("TimeoutError while connecting to MySQL:".format(e))
    except TypeError as e:
        print("TypeError while connecting to MySQL:".format(e))
        
def getListId(parameters):
    idRunList = list()
    with openConnection(parameters) as connector:
        with getCursorIDDataByConnector(parameters.table, connector) as cursor:
            loadedIdRunList = cursor.fetchall()
            for id_RUN in loadedIdRunList:
                idRunList.append(id_RUN[0])
    result = {}
    result['id_RUN'] = idRunList
    return result

def getRunId(id,sqlParameters):
    with openConnection(sqlParameters) as connector:
        strQuery = ("SELECT {0} FROM {1} WHERE {2} = {3}".format(
            TABLE_1FIELD_NAME,
            sqlParameters.table,
            TABLE_1FIELD_NAME,
            id))

        try:
            cursor = connector.cursor()
            cursor.execute(strQuery)
            loadedResult=cursor.fetchall()
            if (len(loadedResult)==0):
                print ("error")
            return loadedResult[0][0]
        except TimeoutError as e:
            print("TimeoutError while connecting to MySQL:".format(e))
        except TypeError as e:
            print("TypeError while connecting to MySQL:".format(e))
    
def getListInfo(parameters):
    idRunList = list()
    acsnList = list()
    dateTime = list()
    timeSliceB1 = list()
    delayB1 = list()
    timeSliceB2 = list()
    delayB2 = list()
    with openConnection(parameters) as connector:
        with getCursorWODataByConnector(parameters, connector) as cursor:
            for (id_RUN,ACSN,Date_Time,TimeSlice_B1, Delay_B1, TimeSlice_B2, Delay_B2) in cursor:
                idRunList.append(id_RUN)
                acsnList.append(ACSN)
                dateTime.append(Date_Time)
                timeSliceB1.append(TimeSlice_B1)
                delayB1.append(Delay_B1)
                timeSliceB2.append(TimeSlice_B2)
                delayB2.append(Delay_B2) 
    result = {}
    result['id_RUN'] = idRunList
    result['ACSN'] = acsnList
    result['Date_Time'] = dateTime
    result['TimeSlice_B1'] = timeSliceB1
    result['Delay_B1'] = delayB1
    result['TimeSlice_B2'] = timeSliceB2
    result['Delay_B2'] = delayB2
    return result
                      
if __name__ == "__main__":
    parameters = ParametersConnection(
        user = "viewer",
        password = "HereJustToSee",
        host = "ma-s.jinr.ru",
        database = "TIC",
        table = "session_test2",
        port = 3306
        )
    print(parametersIsValid(parameters))