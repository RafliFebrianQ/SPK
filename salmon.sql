PGDMP         %    
        	    {            Salmon    10.23    10.23 
    �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �
           1262    16433    Salmon    DATABASE     �   CREATE DATABASE "Salmon" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_Indonesia.1252' LC_CTYPE = 'English_Indonesia.1252';
    DROP DATABASE "Salmon";
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �
           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �
           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    16434    salmon    TABLE     �   CREATE TABLE public.salmon (
    vektor character varying NOT NULL,
    harga integer NOT NULL,
    umur character varying NOT NULL,
    berat character varying NOT NULL,
    lemak character varying NOT NULL,
    "omega-3" character varying NOT NULL
);
    DROP TABLE public.salmon;
       public         postgres    false    3            �
          0    16434    salmon 
   TABLE DATA               N   COPY public.salmon (vektor, harga, umur, berat, lemak, "omega-3") FROM stdin;
    public       postgres    false    196   }       �
   ~   x�5��!C�v1�|�^���/m�8`)v�S���,�X,����A�B�TY��,��WYs}�Gf��l�%$��
�=�hc�NY��K0|�V��oنhK��ͼ�8�����|��ll~�H&$�     