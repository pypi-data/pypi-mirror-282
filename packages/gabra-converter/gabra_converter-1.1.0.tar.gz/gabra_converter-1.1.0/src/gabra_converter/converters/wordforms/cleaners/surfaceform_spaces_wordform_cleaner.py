'''
Skip any wordforms whose surfaceform contains spaces.
'''

from gabra_converter.converters.wordforms.row.wordform_row import WordformRow
from gabra_converter.converters.wordforms.cleaners.wordform_cleaner import WordformCleaner


__all__ = [
    'SurfaceformSpacesWordformCleaner',
]


#########################################
class SurfaceformSpacesWordformCleaner(WordformCleaner):
    '''
    Skip any wordforms whose surfaceform contains spaces.
    '''

    #########################################
    def __init__(
        self,
    ) -> None:
        '''
        Initialiser.
        '''
        super().__init__(
            id_='surfaceform_spaces',
            description='Skip any wordforms whose surfaceform contains spaces.',
        )

    #########################################
    def clean(
        self,
        row: WordformRow, # pylint: disable=unused-argument
        lexemes_id_map: dict[str, int], # pylint: disable=unused-argument
    ) -> bool:
        '''
        Clean a row using a particular process.

        :param row: A wordform row to be checked and cleaned.
        :param lexemes_id_map: A dictionary mapping the original lexeme hexademical unique IDs to
            their given decimal unique IDs.
        :return: Whether the row passes the cleaner's filter.
            A False indicates that it should be skipped.
        '''
        return ' ' not in row.surface_form
