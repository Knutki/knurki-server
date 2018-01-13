from flask import Flask


def SOURCES(app: Flask):
    def build_sources(*sources_list):
        for blueprint in sum(sources_list, []):
            app.register_blueprint(blueprint, url_prefix='/' + blueprint.name)
    return build_sources
