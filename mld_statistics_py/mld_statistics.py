#-*- coding: utf-8-*-

def _cls_patterns(lines):
    labels = int(lines[2].strip().split(' ')[-1])
    data = lines[3:]
    return list(map(lambda x: ''.join(x.strip().split(' ')[-6:]), data))

def _DL(lines):
    """
    Distinct Label Set (DL) is the total count of number of distinct label combinations observed in the dataset
    """
    return len(set(_cls_patterns(lines)))

def _PDL(lines, dl):
    """
    Proportion of DistinctLabel Set(PDL)isthenormalizedDistinctLabelSet,normal-ized by total number of examples
    """
    return float(dl)/len(lines[3:])


def _LCard(lines):
    """
    Label Cardinality (LCard) is the average number of labels per example
    """
    patterns = _cls_patterns(lines)
    return float(sum(map(lambda x: x.count('1') ,patterns)))/len(patterns)

def _LDen(lines):
    """
    Label Density (LDen) is LCard normalized by the the number of labels
    """
    labels = int(lines[2].strip().split(' ')[-1])
    return float(_LCard(lines))/labels

def MdlSta(datafilename):
    datafilename = "data/" + datafilename
    datafile = open(datafilename)
    lines = datafile.readlines()


    print('\n ------------ Multi-label dataset Statistics ------------\n')
    _dl = _DL(lines)
    print('Distinct Label Set (DL): %d\n'%_dl)
    print('Proportion of Distinct Label Set (PDL): %.2f\n' % _PDL(lines,_dl))
    print('Label Cardinality (LCard): %.2f\n' % _LCard(lines))
    print('Label Density (LDen): %.2f\n' % _LDen(lines))
    print('--------------------------------------------------------\n')
