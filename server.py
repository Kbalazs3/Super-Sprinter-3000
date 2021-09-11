from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', user_stories=user_stories)


@app.route("/story", methods=["GET", "POST"])
def render_add_new_story():
    return render_template("add_new_user_story.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    title = format(request.form['st'])
    us_story = format(request.form["user_story"])
    acceptance = format(request.form["acceptance_criteria"])
    bus_val = format(request.form["business_value"])
    estimate = format(request.form["estimation"])
    new_data_list = add_to_dictionary_and_list(title, us_story, acceptance, bus_val, estimate)
    data_handler.write_all_user_story(new_data_list)
    return redirect("/")


def add_to_dictionary_and_list(title, us_story, acceptance, bus_val, estimate):
    read_data = data_handler.get_all_user_story()
    new_story = {}
    pid = data_handler.generate_id()
    new_story['id'] = int(pid)
    new_story['title'] = title
    new_story['user_story'] = us_story
    new_story['acceptance_criteria'] = acceptance
    new_story['business_value'] = bus_val
    new_story['estimation'] = estimate
    new_story['status'] = 'planning'
    read_data.append(new_story)
    return read_data


@app.route("/submit-update",  methods=['POST'])
def submit_update():
    dict = {}
    dict['title']= request.form['st']
    dict['user_story'] = request.form['user_story']
    dict['acceptance_criteria']= request.form['acceptance_criteria']
    dict['business_value'] = request.form['business_value']
    dict['estimation'] = request.form['estimation']
    dict['status'] = request.form['status']
    dict['id'] = request.form['id']
    data_handler.update_data(dict)
    return redirect('/')


@app.route("/update-story/<int:pid>")
def update_user_story(pid):
    dicts = data_handler.get_element_by_id(pid)
    return render_template("update_user_story.html", d=dicts)


if __name__ == '__main__':
    app.run(
    # host='0.0.0.0'

    port=8000,
    debug=True,
    )
