import torch

configurations = {
    1: dict(
        SEED = 1337, # random seed for reproduce results
        
        SYNC_DATA = True,
        SYNC_DATA_NUMCLASS = 1300000,
        DATA_ROOT = '../data/ms1m-retinaface-t1', # the parent root where your train/val/test data are stored
        VAL_SET = 'lfw, cfp_fp, agedb_30', # validation set name
        MODEL_ROOT = '../models/tmp/model', # the root to buffer your checkpoints
        IS_RESUME = False,
        BACKBONE_RESUME_ROOT = "",
        HEAD_RESUME_ROOT = "",
        
        BACKBONE_NAME = 'IR_50', # support: ['MobileFaceNet', 'ResNet_50', 'ResNet_101', 'ResNet_152', 
                                #'IR_50', 'IR_101', 'IR_152', 'IR_SE_50', 'IR_SE_100', 'IR_SE_101', 'IR_SE_152',
                                #'AttentionNet_IR_56', 'AttentionNet_IRSE_56','AttentionNet_IR_92', 'AttentionNet_IRSE_92',
                                #'ResNeSt_50', 'ResNeSt_101', 'ResNeSt_100']
        HEAD_NAME = "ArcFace", # support:  ['Softmax', 'ArcFace', 'CosFace', 'SphereFace', 'Am_softmax', 'ArcNegFace', 'CurricularFace', 'SVX']
        LOSS_NAME = 'CrossEntropy', # support: [''CrossEntropy', Focal', 'HardMining', 'LabelSmooth', 'Softplus']
        
        INPUT_SIZE = [112, 112], # support: [112, 112] and [224, 224]
        RGB_MEAN = [0.5, 0.5, 0.5], # for normalize inputs to [-1, 1]
        RGB_STD = [0.5, 0.5, 0.5],
        EMBEDDING_SIZE = 512,
        BATCH_SIZE = 1024,
        EVAL_FREQ = 2000, #for ms1m, batch size 1024, EVAL_FREQ=2000
        DROP_LAST = True, # whether drop the last batch to ensure consistent batch_norm statistics
        
        OPTIMIZER = 'sgd', # sgd, adam, lookahead, radam, ranger, adamp, sgdp
        LR = 0.1,
        LR_SCHEDULER = 'cosine', # step/multi_step/cosine
        WARMUP_EPOCH = 0, 
        WARMUP_LR = 0.0,
        START_EPOCH = 0,
        NUM_EPOCH = 16,
        LR_STEP_SIZE = 10, 
        LR_DECAY_EPOCH = [10, 18, 22],
        LR_DECAT_GAMMA = 0.1,
        LR_END = 1e-5,
        WEIGHT_DECAY = 5e-4,
        MOMENTUM = 0.9,
        
        WORLD_SIZE = 1,
        RANK = 0,
        GPU = [0,1,2,3,4,5,6,7], # specify your GPU id
        DIST_BACKEND = 'nccl',
        DIST_URL = 'tcp://localhost:23456',
        NUM_WORKERS = 2,
        TEST_GPU_ID = [0,1,2,3,4,5,6,7],

        USE_AMP = True,
        OPT_LEVEL = 'O2',
        SYNC_BN = False,

        # Data Augmentation
        RANDAUGMENT = False,
        RANDAUGMENT_N = 2, # random pick numer of aug typr form aug_list 
        RANDAUGMENT_M = 9,
        RANDOM_ERASING = False,
        MIXUP = False,
        MIXUP_ALPHA = 1.0,
        MIXUP_PROB = 0.5,
        CUTOUT = False, 
        CUTMIX = False, 
        CUTMIX_ALPHA = 1.0,
        CUTMIX_PROB = 0.5,
        COLORJITTER = False
    ),
}
