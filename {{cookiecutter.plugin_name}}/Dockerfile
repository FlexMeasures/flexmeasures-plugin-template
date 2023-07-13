FROM lfenergy/flexmeasures

# Install requirements, e.g. like this
#COPY requirements/app.in /app/requirements/{{cookiecutter.module_name}}.txt
#RUN pip3 install --no-cache-dir -r requirements/{{cookiecutter.module_name}}.txt

COPY {{cookiecutter.module_name}}/ /app/{{cookiecutter.module_name}}
# Make sure FlexMeasures recognizes this plugin (requires FlexMeasures v0.14)
ENV FLEXMEASURES_PLUGINS="/app/{{cookiecutter.module_name}}"
