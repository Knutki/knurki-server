from flask import Flask


def SOURCES(prefix: str, app: Flask):
    url_prefix = '/' if prefix == '' else '/{}/'.format(prefix)

    def build_sources(*sources_list):
        for blueprint in sum(sources_list, []):
            app.register_blueprint(blueprint, url_prefix=url_prefix + blueprint.name)

    return build_sources
