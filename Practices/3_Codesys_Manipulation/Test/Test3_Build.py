APPLICATION_NAME = "Application"

proj = projects.primary
# Find the first Application object in the project
applications = proj.find(APPLICATION_NAME, recursive=True)

if not applications:
    print("No Application found in the project!")
else:
    app = applications[0]
    print("Is active application", app.is_active_application)
    if app.is_active_application:
        app.clean()
        app.build()
        print('Built successfully')
