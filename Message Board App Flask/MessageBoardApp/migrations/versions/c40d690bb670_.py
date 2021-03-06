"""empty message

Revision ID: c40d690bb670
Revises: 
Create Date: 2020-04-19 23:20:38.633692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c40d690bb670'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_title', sa.String(length=50), nullable=False),
    sa.Column('activity_details', sa.String(length=100), nullable=False),
    sa.Column('activity_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_activities_activity_details'), 'activities', ['activity_details'], unique=True)
    op.create_index(op.f('ix_activities_activity_title'), 'activities', ['activity_title'], unique=True)
    op.create_table('budget',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_budget', sa.Float(), nullable=False),
    sa.Column('current_cost', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projectstatus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_planning', sa.Boolean(), nullable=False),
    sa.Column('project_design', sa.Boolean(), nullable=False),
    sa.Column('project_development', sa.Boolean(), nullable=False),
    sa.Column('project_testing', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('project_title', sa.String(length=30), nullable=False),
    sa.Column('project_description', sa.String(length=100), nullable=False),
    sa.Column('project_start_date', sa.DateTime(), nullable=False),
    sa.Column('project_end_date', sa.DateTime(), nullable=True),
    sa.Column('project_expected_end_date', sa.DateTime(), nullable=False),
    sa.Column('project_status_id', sa.Integer(), nullable=True),
    sa.Column('project_finance_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_finance_id'], ['budget.id'], ),
    sa.ForeignKeyConstraint(['project_status_id'], ['projectstatus.id'], ),
    sa.PrimaryKeyConstraint('project_id')
    )
    op.create_index(op.f('ix_projects_project_description'), 'projects', ['project_description'], unique=True)
    op.create_index(op.f('ix_projects_project_title'), 'projects', ['project_title'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('designation', sa.String(length=30), nullable=False),
    sa.Column('reports_to_id', sa.Integer(), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('associated_project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['associated_project_id'], ['projects.project_id'], ),
    sa.ForeignKeyConstraint(['reports_to_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_first_name'), 'users', ['first_name'], unique=False)
    op.create_index(op.f('ix_users_last_name'), 'users', ['last_name'], unique=False)
    op.create_index(op.f('ix_users_password'), 'users', ['password'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('Activity_association',
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('activities_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activities_id'], ['activities.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], )
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=20), nullable=False),
    sa.Column('message', sa.String(length=50), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Notification_association',
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('notification_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['notification_id'], ['notification.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Notification_association')
    op.drop_table('notification')
    op.drop_table('Activity_association')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_password'), table_name='users')
    op.drop_index(op.f('ix_users_last_name'), table_name='users')
    op.drop_index(op.f('ix_users_first_name'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_projects_project_title'), table_name='projects')
    op.drop_index(op.f('ix_projects_project_description'), table_name='projects')
    op.drop_table('projects')
    op.drop_table('projectstatus')
    op.drop_table('budget')
    op.drop_index(op.f('ix_activities_activity_title'), table_name='activities')
    op.drop_index(op.f('ix_activities_activity_details'), table_name='activities')
    op.drop_table('activities')
    # ### end Alembic commands ###
