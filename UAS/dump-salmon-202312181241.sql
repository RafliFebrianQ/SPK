PGDMP     !    )                {            salmon    10.23    10.23     �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �
           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3            �            1259    16542    salmon    TABLE     �   CREATE TABLE public.salmon (
    id_salmon character varying NOT NULL,
    harga integer NOT NULL,
    umur integer NOT NULL,
    berat integer NOT NULL,
    lemak integer NOT NULL,
    omega_3 integer NOT NULL
);
    DROP TABLE public.salmon;
       public         postgres    false    3            �
          0    16542    salmon 
   TABLE DATA               O   COPY public.salmon (id_salmon, harga, umur, berat, lemak, omega_3) FROM stdin;
    public       postgres    false    196   �       �
   h   x�U��	�0ϫb�>kG�%]�����w�0�hbMU�@�!{�3	�]���h��?��'iK����M��y2cw��<�j)A���7�==S}�s���Bq     