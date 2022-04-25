def test_index_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that hte response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data

def test_about_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that hte response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that hte response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"VTM Estimator" in res.data

def test_vtm_estimate(app, client):
    """ 
    GIVEN a user enters the tank radius as 180 inches and tank height as 360 inches
    WHEN those values are passed to this function
    THEN the general estimate for painting the tank is accurately calculated as $141,300.00
    """
    print("\r")
    print(" -- estimate unit test")
    with app.test_client() as test_client:
        estimate = {"radius":"180", "height":"360"}
        res = test_client.post('/estimate', data=estimate)
        assert res.status_code == 200
        assert b"141,300.00" in res.data