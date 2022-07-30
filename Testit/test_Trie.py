import MIDIscape.Trie
import pytest

lista=MIDIscape.Trie.luoTrie(1)

def tarkistaPituus():
    assert len(lista) == 14