import mysql.connector
import streamlit as st

#connexion au bd

conn = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "root",
    db = "DGI_DB",
)

c = conn.cursor()

def voire_touts_data():
    c.execute('select * from base_de_donnees order by id asc')
    data = c.fetchall()
    return data