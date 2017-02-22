import pyramid_handlers
from blueyellow_pycharm_app.controllers.base_controller import BaseController
from blueyellow_pycharm_app.services.albums_service import AlbumsService

class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer = 'templates/albums/index.pt')
    def index(self):
        all_albums = AlbumsService.get_albums()

        return {'albums': all_albums}