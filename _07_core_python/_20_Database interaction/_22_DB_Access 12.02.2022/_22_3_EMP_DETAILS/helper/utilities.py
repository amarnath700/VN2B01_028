'''
Created on Dec 23, 2019

@author: madhu
'''
import psycopg2

conn = psycopg2.connect(database="postgres", 
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
PATIENT_CREATE = 'create table Patient_Info(pid,name....)'