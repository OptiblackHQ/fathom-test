import streamlit as st
import pandas as pd
import requests
import json

# Streamlit app
st.title("Display Data from API as DataFrame")

# URL and headers for the API
api_url = 'https://fathom.video/calls/previous'
headers = {
    'accept': 'application/json, text/plain, */*',
    'cookie': '_gcl_au=1.1.2123438393.1726632695; _CEFT=EgNwlgpg7hAmBcBbAzgRQDYFYBWAxAngEoAiA9gNAByACgE6WIBSAggIwC0mAmkA; hubspotutk=fd8735e9368c2dfe479438ec46f66447; muxData=mux_viewer_id=2e1a24ff-b111-47a4-b3f2-e4af4678e146&msn=0.3036848760052615&sid=d0793eeb-6fab-49b1-9e0c-698b164397ce&sst=1728559596974.8&sex=1728561100440.9; cebs=1; _ce.clock_event=1; __hstc=60514354.fd8735e9368c2dfe479438ec46f66447.1727449140348.1728285101338.1728559603368.4; __hssrc=1; __hssc=60514354.1.1728559603368; _fathom_session=85baade50fd3493ef582372b2df21b34; cf_clearance=hOR_Vh9PbtYD0c.4_2wTC06at8SoBlzPYuQR5_rOtCw-1728559627-1.2.1.1-.ZhyUk46pJoi.cljxF0tc37tAfLNmwY3LGDPp0oeO51QjJGyHdS8zzHJUgH7AzXOyM6cXoEWbg4mrOEkfd_CCwvLX_RcLDIX0RsAy_UMQuAulf2.rgWGMcfboLkf_Kiu.dCTCN79DqfO1qZwvqRC8Ft0BnTir.fXjfZsruSowmfU247OoARUGs3K7clSKWywggUxltyqfXCTaIgAcwesO6Qid5sqjANWEE7tl3XfhhY8hRM0NHPE1oee8gYebEVvMt5WvduI9._r4zVe1eW3S6OeRfbyj1XY6vzaVpcSQCZtry94hoHy6QLnHLQh8KqbHGerUILN8daMgsIyrXAUw1svXNFAzWgy4XGGxT9_6XO46bjD4.q6PvdC9m715mh6LtN8yaDUf57lZoLYiVaBTdOBWirC687KFTgNeQXxk2U; _ce.clock_data=-18%2C49.36.16.29%2C2%2Cbcf703f9beb5549241b94bb67f4e9ac0%2CChrome%2CIN; cebsp_=4; _ce.s=v~9161963178417556f5bb4b33c9fa1a2617c8e30f~lcw~1728559710315~lva~1728559710311~vpv~9~v11slnt~1727690045700~vir~returning~flvl~%2CmsQl5jFyRDo%3ANPrNmJA1-5Y~v11ls~04e2bd80-856e-11ef-8564-1f793e88a6f5~gtrk.la~m237tjja~v11.sla~1728559708968~v11.fhb~1728559612789~v11.lhb~1728559710315~v11.cs~431579~v11.s~8c70e690-86fa-11ef-a795-6f0c43c4dd68~lcw~1728559710317; XSRF-TOKEN=W3XPSNsrefoJWuBC2uFtsXqgYo%2Fx7eBM8GtZiuN%2FOVng5E9aWaCu38xi%2FcMZbz9GrXD0Zv6py9wSniCM%2FmSclQ%3D%3D',
    'priority': 'u=1, i',
    'referer': 'https://fathom.video/home',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    'x-xsrf-token': 'W3XPSNsrefoJWuBC2uFtsXqgYo/x7eBM8GtZiuN/OVng5E9aWaCu38xi/cMZbz9GrXD0Zv6py9wSniCM/mSclQ=='
}

# Fetch data from the API
try:
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    if response.content:
        data = response.json()
        
        # Convert data to DataFrame
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame([data])
        
        # Display DataFrame as a table in Streamlit
        st.dataframe(df)
    else:
        st.warning("No data available from the API.")
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")
except json.JSONDecodeError as e:
    st.error(f"Error decoding JSON response: {e}")
