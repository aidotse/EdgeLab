FROM nvcr.io/nvidia/pytorch:21.03-py3

ARG u_id
ARG g_id
ARG username

RUN python3 -m pip install --upgrade pip

RUN pip install -e git://github.com/scaleoutsystems/fedn.git@v0.2.5#egg=fedn\&subdirectory=fedn

RUN groupadd --gid ${g_id} ${username}
RUN useradd --uid ${u_id} --gid ${g_id} --shell /bin/bash --create-home ${username}
USER ${username}
RUN chown -R ${u_id}:${g_id} /home/${username}
RUN chmod -R  755 /home/${username}

WORKDIR /home/${username}
