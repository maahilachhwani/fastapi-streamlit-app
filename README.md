# fastapi-streamlit-app

(myenv) C:\Users\Admin\Downloads>cd fastapi-streamlit-app

(myenv) C:\Users\Admin\Downloads\fastapi-streamlit-app>pip install fastapi uvicorn streamlit
Collecting fastapi
  Downloading fastapi-0.116.0-py3-none-any.whl.metadata (28 kB)
Collecting uvicorn
  Downloading uvicorn-0.35.0-py3-none-any.whl.metadata (6.5 kB)
Requirement already satisfied: streamlit in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (1.46.1)
Collecting starlette<0.47.0,>=0.40.0 (from fastapi)
  Downloading starlette-0.46.2-py3-none-any.whl.metadata (6.2 kB)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from fastapi) (2.11.7)
Requirement already satisfied: typing-extensions>=4.8.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from fastapi) (4.14.1)
Requirement already satisfied: annotated-types>=0.6.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi) (2.33.2)
Requirement already satisfied: typing-inspection>=0.4.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi) (0.4.1)
Requirement already satisfied: anyio<5,>=3.6.2 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from starlette<0.47.0,>=0.40.0->fastapi) (4.9.0)
Requirement already satisfied: idna>=2.8 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi) (3.10)
Requirement already satisfied: sniffio>=1.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi) (1.3.1)
Requirement already satisfied: click>=7.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from uvicorn) (8.2.1)
Requirement already satisfied: h11>=0.8 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from uvicorn) (0.16.0)
Requirement already satisfied: altair<6,>=4.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker<2,>=1.5.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=4.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (6.1.0)
Requirement already satisfied: numpy<3,>=1.23 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (2.3.1)
Requirement already satisfied: packaging<26,>=20 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (24.2)
Requirement already satisfied: pandas<3,>=1.4.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (2.3.1)
Requirement already satisfied: pillow<12,>=7.1.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf<7,>=3.20 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (6.31.1)
Requirement already satisfied: pyarrow>=7.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (20.0.0)
Requirement already satisfied: requests<3,>=2.27 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (2.32.4)
Requirement already satisfied: tenacity<10,>=8.1.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml<2,>=0.10.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (0.10.2)
Requirement already satisfied: watchdog<7,>=2.1.5 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (3.1.44)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from streamlit) (6.5.1)
Requirement already satisfied: jinja2 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from altair<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from altair<6,>=4.0->streamlit) (4.24.0)
Requirement already satisfied: narwhals>=1.14.2 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from altair<6,>=4.0->streamlit) (1.46.0)
Requirement already satisfied: colorama in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from click>=7.0->uvicorn) (0.4.6)
Requirement already satisfied: gitdb<5,>=4.0.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from requests<3,>=2.27->streamlit) (3.4.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from requests<3,>=2.27->streamlit) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from requests<3,>=2.27->streamlit) (2025.6.15)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)
Requirement already satisfied: attrs>=22.2.0 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2025.4.1)
Requirement already satisfied: referencing>=0.28.4 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.26.0)
Requirement already satisfied: six>=1.5 in c:\users\admin\anaconda3\envs\myenv\lib\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)
Downloading fastapi-0.116.0-py3-none-any.whl (95 kB)
Downloading starlette-0.46.2-py3-none-any.whl (72 kB)
Downloading uvicorn-0.35.0-py3-none-any.whl (66 kB)
Installing collected packages: uvicorn, starlette, fastapi
Successfully installed fastapi-0.116.0 starlette-0.46.2 uvicorn-0.35.0


(myenv) C:\Users\Admin\Downloads\fastapi-streamlit-app>uvicorn main:app --reload
←[32mINFO←[0m:     Will watch for changes in these directories: ['C:\\Users\\Admin\\Downloads\\fastapi-streamlit-app']
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m1900←[0m] using ←[36m←[1mStatReload←[0m
←[32mINFO←[0m:     Started server process [←[36m19852←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
←[32mINFO←[0m:     127.0.0.1:58538 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[31m404 Not Found←[0m
←[32mINFO←[0m:     127.0.0.1:58542 - "←[1mPOST /todos/ HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58543 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58544 - "←[1mGET /todos/2 HTTP/1.1←[0m" ←[31m404 Not Found←[0m
←[32mINFO←[0m:     127.0.0.1:58546 - "←[1mPOST /todos/ HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58547 - "←[1mGET /todos/2 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58550 - "←[1mGET /todos/2 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58554 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58557 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58558 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58559 - "←[1mPUT /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58568 - "←[1mGET /docs HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58568 - "←[1mGET /openapi.json HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58576 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58577 - "←[1mGET /todos/1 HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:58578 - "←[1mDELETE /todos/2 HTTP/1.1←[0m" ←[32m200 OK←[0m



(myenv) C:\Users\Admin\Downloads\fastapi-streamlit-app>  streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.18.67:8501


![image](https://github.com/user-attachments/assets/dd35289b-26a9-4075-9084-d1d3348a33c2)
![image](https://github.com/user-attachments/assets/0d9e14fa-ef74-477b-ab41-846e187e2b3d)

http://127.0.0.1:8000/docs#/default/read_todo_item_todos__todo_id__get



