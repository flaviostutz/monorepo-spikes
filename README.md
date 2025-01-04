# python-some

This is a reference Monorepo using a good set of build, lint, test practices for Python projects (will be expanded to other languages later).

Look for a reference Python project at [/shared/libs/hello_world](shared/libs/hello_world/). It has good build, lint and test practices.

## Monorepo features

- Support for multiple languages in packages (NodeJS, Python etc)

- Packages are organized in

  - /shared - packages that can be reused by services
    - Can group shared resources by folders, such as "/makefiles", "/tools", "/schemas"

  - /services - packages that can use shared resources
    - one service shouldn't depend on each other to avoid confusion
    - Can have an inner structure if it's needed to group multiple packages together, such as "orders-service", "driver-service"

- The packages uses a common tooling, but they can also deviate if needed
  - It means that they might use different build, test, lint and deploy tools
  - This is important because when we are migrating to new stacks we should be able to migrate in phases, while handling diversity in parallel

- Each package has its own Makefile as the entry point for all it's operations during development/ci/deployment phases (check [common-targets spec](https://github.com/flaviostutz/common-targets))
  - This makes things much more sane while the developer switches to different projects, regardless of the stack/tooling/language being used :)

