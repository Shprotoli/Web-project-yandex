from backend.db.repositories.blitz_repository import BlitzRepository


class BlitzService:
    def __init__(self, blitz_repository: BlitzRepository):
        self.blitz_repository = blitz_repository