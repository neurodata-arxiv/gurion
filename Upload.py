import ndio.convert.nifti as ndnii #import nifti workflow
print 'imported nifti convert'

data = ndnii.load("Fear199_400_600_1850_2050_450_550_res2_anno.nii") #numpy array from my file
print 'made numpy array'

print data.shape #check array shape

import ndio.remote.neurodata as ND #import neurodata
print 'imported neurodata remote'

oo = ND() #instantiate neurodata
print 'instance of neurodata created'

#oo.delete_channel("Fear199", "GLMannotation")
#print 'deleted fucked up channel'

oo.create_channel('Fear199', 'GLMAnnotationFixed', oo.ANNOTATION, 'uint32', False) #make channel to add annotation
print 'created new channel'

oo.post_cutout('Fear199', 'GLMAnnotationFixed', 0, 0, 0, data, 2) #token, channel, z, x, y, data, resolution
print 'uploaded data to channel'

print 'done'
