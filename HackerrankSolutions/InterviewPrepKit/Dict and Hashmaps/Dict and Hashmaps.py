def checkMagazine(magazine, note):
    for iNote in range(len(note)):
        for iMag in range(len(magazine)):
            if note[iNote] == magazine[iMag]:
                note[iNote] = '@'
                magazine[iMag] = '#'

    if note.count('@') == len(note):
        return 'Yes'
    return 'No'



def checkaMagazine1(magazine, note):
    for iMag in range(len(magazine)):
        for iNote in range(len(note)):
            if note[iNote] == magazine[iMag]:
                note.remove(note[iNote])
                break
    return len(note) == 0


print(checkaMagazine1(['apgo','clm','w','lxkvg','mwz','elo','bg','elo','lxkvg','elo','apgo','apgo','w','elo','bg'], ['elo','lxkvg','bg','mwz','clm','w']))

from collections import Counter


def ransom_note(magazine, rasom):
    if (Counter(rasom) - Counter(magazine)) == {}:
        return 'Yes'
    else:
        return 'No'
