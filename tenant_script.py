from tenant_model.models import ClientModel, DomainModel

# Create your public tenant

tenant = ClientModel(schema_name='public',
                     name='Schemas Inc.',
                     paid_until='2016-12-05',
                     on_trial=False)
tenant.save()

# Create domain for public tenant

domain = DomainModel()
domain.domain = 'localhost'  # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()


"""Create your first real tenant"""

# tenant = ClientModel(schema_name='mindbowser',
#                      name='Mindbowser Inc.',
#                      paid_until='2023-12-25',
#                      on_trial=True)
# tenant.save()  # migrate_schemas automatically called, your tenant is ready to be used!

# Create domain for real tenant

# domain = DomainModel()
# domain.domain = 'mindbowser.com'  # don't add your port or www here!
# domain.tenant = tenant
# domain.is_primary = True
# domain.save()
