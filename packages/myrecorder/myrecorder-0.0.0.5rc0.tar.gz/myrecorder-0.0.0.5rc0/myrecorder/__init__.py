import os
import streamlit as st
import streamlit.components.v1 as components
import base64

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component("myrecorder",url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("myrecorder", path=build_dir)

def recorder(start_prompt="Start recording",stop_prompt="Stop recording",just_once=False,use_container_width=False,format="webm",callback=None,args=(),kwargs={},key=None):
    if not '_last_mic_recorder_audio_id' in st.session_state:
        st.session_state._last_mic_recorder_audio_id=0
    if key and not key+'_output' in st.session_state:
        st.session_state[key+'_output']=None
    new_output=False
    component_value = _component_func(start_prompt=start_prompt,stop_prompt=stop_prompt,use_container_width=use_container_width,format=format,key=key,default=None)
    if component_value is None:
        output=None
    else:
        id=component_value["id"]
        new_output=(id>st.session_state._last_mic_recorder_audio_id)
        if new_output or not just_once:
            audio_bytes=base64.b64decode(component_value["audio_base64"])
            sample_rate=component_value["sample_rate"]
            sample_width=component_value["sample_width"]
            format=component_value["format"]
            output={"bytes":audio_bytes,"sample_rate":sample_rate,"sample_width":sample_width,"format":format,"id":id}
            st.session_state._last_mic_recorder_audio_id=id
        else:
            output=None
    if key:
        st.session_state[key+'_output']=output
    if new_output and callback:
        callback(*args,**kwargs)
    return output