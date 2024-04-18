from webapp.app import create_app, AppConfig


def main():
    """Main entrypoint for running the Flask application"""
    config = AppConfig.from_env()
    app = create_app(config)
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
