# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .auth import (
    CreateUserSuccessView,
    CreateUserView,
)

from .error import (
    ErrorDetailsView,
)

from .post import (
    CreatePostView,
    DeletePostView,
    EditPostView,
    GetPostsByTitleView,
    MyPostsListView,
    PostListView,
    SuccessfulPostDetailView,
    PostDetailView,
)

from .redirect import (
    RedirectView,
)
