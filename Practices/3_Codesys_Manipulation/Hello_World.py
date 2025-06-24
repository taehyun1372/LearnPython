proj = projects.primary

if proj is None:
    print("No project is currently opened!")
else:
    # Find the first Application object in the project
    applications = proj.find('Application', recursive=True)

    if not applications:
        print("No Application found in the project!")
    else:
        app = applications[0]
        print("Application name:", app.name)
