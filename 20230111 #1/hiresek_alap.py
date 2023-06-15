class Celeb:
    name = ''
    job = ''
    nationality = ''
    
    def nemzetiseg(self):
        if self.nationality == 'a':
            return 'Ms.'
        elif self.nationality == 'n':
            return 'Frau'
        return False
