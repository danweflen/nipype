# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.dti import DTLUTGen
def test_DTLUTGen_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inversion=dict(units='NA',
    argstr='-inversion %d',
    ),
    frange=dict(argstr='-frange %s',
    units='NA',
    position=1,
    ),
    acg=dict(argstr='-acg',
    ),
    out_file=dict(position=-1,
    genfile=True,
    argstr='> %s',
    ),
    trace=dict(units='NA',
    argstr='-trace %G',
    ),
    args=dict(argstr='%s',
    ),
    watson=dict(argstr='-watson',
    ),
    scheme_file=dict(position=2,
    mandatory=True,
    argstr='-schemefile %s',
    ),
    step=dict(units='NA',
    argstr='-step %f',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    snr=dict(units='NA',
    argstr='-snr %f',
    ),
    lrange=dict(argstr='-lrange %s',
    units='NA',
    position=1,
    ),
    samples=dict(units='NA',
    argstr='-samples %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    bingham=dict(argstr='-bingham',
    ),
    )
    inputs = DTLUTGen.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_DTLUTGen_outputs():
    output_map = dict(dtLUT=dict(),
    )
    outputs = DTLUTGen.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value