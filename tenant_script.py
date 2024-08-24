from tenants.models import TenantModel, DomainModel

# create your public tenant
# tenant = TenantModel(schema_name='public',
#                      name='Schemas Inc.',
#                      paid_until='2016-12-05',
#                      on_trial=False)
# tenant.save()
# #
# # # Add one or more domains for the tenant
# domain = DomainModel()
# domain.domain = 'localhost'  # don't add your port or www here! on a local server you'll want to use localhost here
# domain.tenant = tenant
# domain.is_primary = True
# domain.save()

# create your first real tenant
tenant = TenantModel(schema_name='jupitergroup',
                     name='Jupiter Hospital',
                     paid_until='2024-12-05',
                     on_trial=True)
tenant.save()  # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = DomainModel()
domain.domain = 'jupiter'  # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()

