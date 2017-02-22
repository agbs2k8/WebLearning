import pyramid_handlers
from blueyellow_pycharm_app.controllers.base_controller import BaseController
from blueyellow_pycharm_app.infrastructure.suppressor import suppress


class HomeController(BaseController):
    @pyramid_handlers.action(renderer = 'templates/home/index.pt')
    def index(self):
        return {'value' : 'HOME'}

    @pyramid_handlers.action(renderer = 'templates/home/about.pt')
    def about(self):
        return {'value' : 'ABOUT'}

    @pyramid_handlers.action(renderer = 'templates/home/contact.pt')
    def contact(self):
        return {'value' : 'CONTACT'}

    @suppress
    def dont_expose_as_web_action(self):
        print("Called dont_expose...")