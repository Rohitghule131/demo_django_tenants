from tenant_model.models import ClientModel, DomainModel

# create your public tenant
tenant = ClientModel(schema_name='public',
                     name='Schemas Inc.',
                     paid_until='2016-12-05',
                     on_trial=False)
tenant.save()

# Add one or more domains for the tenant
domain = DomainModel()
domain.domain = 'localhost'  # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()

# create your first real tenant
tenant = ClientModel(schema_name='tenant2',
                     name='Tenant 2',
                     paid_until='2014-12-05',
                     on_trial=True)
tenant.save()  # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = DomainModel()
domain.domain = 'tenant2'  # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()
