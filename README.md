parsely

# This is a work in project

- dockerfile best practice checks:
    - [ ] use multistage builds
    - [ ] pin to semantic minor
    - [ ] use approved image registry, at least for final image
    - [ ] if apt-get or apt exists, make sure apt-get update and apt-get install are in the same RUN statement
    - [ ] using COPY over ADD
    - [ ] don't have root containers (make sure a user is created and used)