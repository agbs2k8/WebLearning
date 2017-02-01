from pyramid.view import view_config
import blueyellow_pycharm_app.utils


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return extend_model({'project': 'blueyellow_pycharm_app'})

def extend_model(model_dict):
    model_dict['build_cache_id'] = blueyellow_pycharm_app.utils.build_cache_id
    return model_dict
