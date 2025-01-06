# monorepo-spikes

This is a reference polyglot monorepo with a set of spikes on project structures, and also employs tasks such as build, lint, test, inter dependency management with packages using different languages but still keeping sanity for the developers :)

## Monorepo features

- Support for multiple languages in packages (NodeJS, Python etc)

- Packages are organized in

  - /shared - packages with shared resources
    - Can group shared resources by folders, such as "/makefiles", "/tools", "/schemas"

  - /apps - packages with applications
    - those packages might use shared resources
    - they are normally microservices that provides frontend or backend services
    - one service shouldn't depend on each other to avoid confusion
    - can have an inner structure if it's needed to group multiple packages together, such as "orders-service", "driver-service"

- Makefiles with a minimum set of targets ([common-targets spec](https://github.com/flaviostutz/common-targets)) are one of the only common structures in the entire monorepo as it can acommodate most of the languages/diversity/stacks, even if being used only as a "proxy" to the actual tools.
  - Each package has its own Makefile as the entry point for all it's operations during development/ci/deployment phases
  - This makes things much more sane while the developer switches to different projects, regardless of the stack/tooling/language being used :)

- The packages uses a common tooling, but they can also deviate if needed
  - It means that they might use different build, test, lint and deploy tools
  - This is important because when we are migrating to new stacks we should be able to migrate in phases, while handling diversity in parallel

