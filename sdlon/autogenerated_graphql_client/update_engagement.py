# Generated by ariadne-codegen on 2024-09-04 09:16
# Source: queries.graphql

from uuid import UUID

from .base_model import BaseModel


class UpdateEngagement(BaseModel):
    engagement_update: "UpdateEngagementEngagementUpdate"


class UpdateEngagementEngagementUpdate(BaseModel):
    uuid: UUID


UpdateEngagement.update_forward_refs()
UpdateEngagementEngagementUpdate.update_forward_refs()
