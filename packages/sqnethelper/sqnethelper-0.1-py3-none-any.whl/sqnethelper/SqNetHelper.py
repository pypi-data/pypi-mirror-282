import click
from .ECSManager import ECSManager
from .ConfigManager import ConfigManager

class SqNetHelper:

    @staticmethod
    def setup(access_key, access_secret):
        config = ConfigManager()
        config.set_config(
            access_key=access_key,
            access_secret=access_secret
        )
        return "配置已保存"

    @staticmethod
    def list_instances():
        config = ConfigManager()
        if not config.is_configured():
            return "Error: 请先设置阿里云凭证"

        try:
            

            ecs_manager = ECSManager(config.access_key, config.access_secret, config.region)
            instances_result = ecs_manager.list_instances()

            if isinstance(instances_result, str) and instances_result.startswith('Error'):
                return instances_result

            if not isinstance(instances_result, dict):
                raise ValueError("Unexpected response from list_instances()")


            output = ["Available ECS Instances:"]
            for i, (instance_id, instance_info) in enumerate(instances_result.items(), start=1):
                public_ip = instance_info['PublicIpAddress'] or 'N/A'
                output.append(f"{i}. ID: {instance_id}, Name: {instance_info['Name']}, Public IP: {public_ip}, Status: {instance_info['Status']}")


            return "\n".join(output)


        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def list_regions():
        config = ConfigManager()
        if not config.is_configured():
            return "Error: 请先设置阿里云凭证", None

        ecs_manager = ECSManager(config.access_key, config.access_secret, config.region)
        regions = ecs_manager.get_regions()
        
        if not regions:
            return "No regions found.", None
        
        output = ["Available regions:"]
        region_choices = []
        for i, (region_id, local_name) in enumerate(regions.items(), start=1):
            region_choices.append(region_id)
            output.append(f"{i}. {local_name} ({region_id})")
        
        return "\n".join(output), region_choices


    @staticmethod
    def set_region(choice, region_choices):
        if choice < 1 or choice > len(region_choices):
            return "Invalid choice."
        
        selected_region = region_choices[choice - 1]
        config = ConfigManager()
        config.set_config(
            region=selected_region
        )
        return f"Region set to {selected_region}"

    @staticmethod
    def create_instance():
        config = ConfigManager()
        if not config.is_configured():
            return "Error: 请先设置阿里云凭证"

        ecs_manager = ECSManager(config.access_key, config.access_secret, config.region)
        instances_result = ecs_manager.create_instance()
        return instances_result
        

    @staticmethod
    def delete_instance():
        config = ConfigManager()
        if not config.is_configured():
            return "Error: 请先设置阿里云凭证", None

        try:
            ecs_manager = ECSManager(config.access_key, config.access_secret, config.region)
            instances_result = ecs_manager.list_instances()

            if isinstance(instances_result, str) and instances_result.startswith('Error'):
                return instances_result, None

            if not isinstance(instances_result, dict):
                raise ValueError("Unexpected response from list_instances()")

            output = ["Available ECS Instances:"]
            instances_choices = []
            for i, (instance_id, instance_info) in enumerate(instances_result.items(), start=1):
                instances_choices.append(instance_id)
                public_ip = instance_info['PublicIpAddress'] or 'N/A'
                output.append(f"{i}. ID: {instance_id}, Name: {instance_info['Name']}, Public IP: {public_ip}, Status: {instance_info['Status']}")

            return "\n".join(output), instances_choices

        except Exception as e:
            return f"Error: {str(e)}", None

    @staticmethod
    def confirm_delete_instance(choice, instances_choices):
        if choice < 1 or choice > len(instances_choices):
            return "Invalid choice. Please enter a valid number."

        instance_id_to_delete = instances_choices[choice - 1]
        config = ConfigManager()
        ecs_manager = ECSManager(config.access_key, config.access_secret, config.region)
        return ecs_manager.delete_instance(instance_id_to_delete)