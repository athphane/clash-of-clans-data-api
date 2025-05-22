from app import FAST_API_PORT, FAST_API_RELOAD
import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        'app.server:app',
        host='0.0.0.0',
        port=FAST_API_PORT,
        reload=FAST_API_RELOAD,
        workers=4
    )